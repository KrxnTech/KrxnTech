#!/usr/bin/env python3
"""Refresh data/contributions.json.

Primary source: GitHub GraphQL (needs GH_TOKEN; the Action's GITHUB_TOKEN works for
public data, a PAT with read:user also counts private contributions).
Fallback: the public contribution calendar page, which needs no token.

Shape written:
{
  "login": "...", "generated_at": "...", "source": "graphql|scrape", "total": 123,
  "days":  [{"date": "YYYY-MM-DD", "count": 3, "level": 0-4}, ...],
  "repos": {"Name": {"description": "...", "stars": 0, "forks": 0,
                     "language": "...", "languages": ["..."], "url": "...", "pushed_at": "..."}}
}
"""
import html
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

LOGIN = os.environ.get("GH_LOGIN", "KrxnTech")
REPOS = [r.strip() for r in os.environ.get("FEATURED_REPOS", "Resume-Buddy,ContentHub").split(",") if r.strip()]
TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
OUT = Path(os.environ.get("CONTRIB_JSON", "data/contributions.json"))
LEVELS = {"NONE": 0, "FIRST_QUARTILE": 1, "SECOND_QUARTILE": 2, "THIRD_QUARTILE": 3, "FOURTH_QUARTILE": 4}


def http(url, data=None, headers=None):
    req = urllib.request.Request(url, data=data, headers=headers or {})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def graphql():
    if not TOKEN:
        raise RuntimeError("no token")
    repo_q = "\n".join(
        f'r{i}: repository(owner:$login,name:"{n}"){{ name description url stargazerCount forkCount pushedAt '
        f'primaryLanguage{{name}} languages(first:4,orderBy:{{field:SIZE,direction:DESC}}){{nodes{{name}}}} }}'
        for i, n in enumerate(REPOS)
    )
    query = f"""query($login:String!){{
      user(login:$login){{ contributionsCollection{{ contributionCalendar{{ totalContributions
        weeks{{ contributionDays{{ date contributionCount contributionLevel }} }} }} }} }}
      {repo_q} }}"""
    body = json.dumps({"query": query, "variables": {"login": LOGIN}}).encode()
    out = json.loads(http("https://api.github.com/graphql", body,
                          {"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json",
                           "User-Agent": "profile-cards"}))
    if "errors" in out and not out.get("data"):
        raise RuntimeError(out["errors"])
    d = out["data"]
    cal = d["user"]["contributionsCollection"]["contributionCalendar"]
    days = [{"date": x["date"], "count": x["contributionCount"], "level": LEVELS[x["contributionLevel"]]}
            for w in cal["weeks"] for x in w["contributionDays"]]
    repos = {}
    for i, n in enumerate(REPOS):
        r = d.get(f"r{i}")
        if r:
            langs = [x["name"] for x in r["languages"]["nodes"]]
            repos[r["name"]] = {"description": r["description"] or "", "stars": r["stargazerCount"],
                                "forks": r["forkCount"], "url": r["url"], "pushed_at": r["pushedAt"],
                                "language": (r["primaryLanguage"] or {}).get("name", ""), "languages": langs}
    return cal["totalContributions"], days, repos


def scrape():
    page = http(f"https://github.com/users/{LOGIN}/contributions", headers={"User-Agent": "profile-cards"})
    counts = {}
    for cid, text in re.findall(r'for="(contribution-day-component-\d+-\d+)"[^>]*>([^<]*)<', page):
        m = re.match(r"\s*(\d+|No) contribution", html.unescape(text))
        if m:
            counts[cid] = 0 if m.group(1) == "No" else int(m.group(1))
    days = []
    for tag in re.findall(r"<td[^>]*data-date[^>]*>", page):
        date = re.search(r'data-date="([^"]+)"', tag).group(1)
        cid = re.search(r'id="([^"]+)"', tag).group(1)
        lvl = int(re.search(r'data-level="(\d)"', tag).group(1))
        days.append({"date": date, "count": counts.get(cid, 0), "level": lvl})
    days.sort(key=lambda x: x["date"])
    if not days:
        raise RuntimeError("calendar not found")
    return sum(d["count"] for d in days), days, {}


def main():
    previous = json.loads(OUT.read_text()) if OUT.exists() else {}
    try:
        total, days, repos = graphql()
        source = "graphql"
    except Exception as e:  # noqa: BLE001
        print(f"graphql unavailable ({e}); falling back to public calendar", file=sys.stderr)
        total, days, repos = scrape()
        source = "scrape"
    repos = {**previous.get("repos", {}), **repos}  # keep last known repo stats if the fallback ran
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({
        "login": LOGIN, "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": source, "total": total, "days": days, "repos": repos}, indent=1) + "\n")
    print(f"wrote {OUT}: {len(days)} days, {total} contributions via {source}")


if __name__ == "__main__":
    main()
