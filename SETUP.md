# Setup guide

## 1. Folder structure
```
KrxnTech/                        <- GitHub profile repository
├── README.md                    <- Main GitHub profile README
├── README (2).md                <- Backup profile README copy
├── assets/                      <- All retro pixel-art SVGs
│   ├── hero.svg, thanks.svg, divider.svg, start.svg, top.svg
│   ├── header-*.svg             Section headings
│   ├── about-photo.svg          Profile photo frame
│   ├── satvistaar-preview.svg   Project 1 screenshot frame
│   ├── resume-buddy-preview.svg Project 2 screenshot frame
│   ├── contenthub-preview.svg   Project 3 screenshot frame
│   ├── window-stats.svg         Stats header frame
│   ├── nav/ cats/ chips/ nums/ contact/
└── tools/build_assets.py        <- Regenerates all SVGs
```

## 2. Profile Links & Handles
| Field | Value |
|---|---|
| GitHub | `KrxnTech` |
| LinkedIn | `krishna-sharma-10b5ab359` |
| Email | `developerkrxna@gmail.com` |
| Portfolio | `https://krxna-tech.vercel.app` |

## 3. Optional: Add custom screenshots
To embed real image screenshots into the retro computer window frames:
```bash
python tools/build_assets.py --photo me.jpg --shot1 satvistaar.png --shot2 resume_buddy.png --shot3 contenthub.png
```
They will be base64-embedded directly into the SVG frames.

## 4. Publish
Commit and push to the `main` branch of `https://github.com/KrxnTech/KrxnTech.git`:
```bash
git add .
git commit -m "Update profile README with LinkedIn and projects"
git push origin main
```
