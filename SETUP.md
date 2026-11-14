# Setup guide

## 1. Folder structure
```
YOUR_GITHUB_USERNAME/            <- repo name MUST equal your GitHub username
├── README.md
├── assets/                      <- all pixel art (generated SVGs)
│   ├── hero.svg, thanks.svg, divider.svg, start.svg, top.svg
│   ├── header-*.svg             section headings
│   ├── about-photo.svg          profile photo frame
│   ├── contenthub-preview.svg   project 1 screenshot frame
│   ├── sigmagpt-preview.svg     project 2 screenshot frame
│   ├── window-stats.svg
│   ├── nav/ cats/ chips/ nums/ contact/
└── tools/build_assets.py        <- regenerates every SVG (optional)
```

## 2. Replace these
| Where | Placeholder | Replace with |
|---|---|---|
| README (stats + contact) | `YOUR_GITHUB_USERNAME` | your GitHub username (Find & Replace all) |
| README (contact) | `YOUR_LINKEDIN_USERNAME` | your LinkedIn handle |
| README (contact) | `YOUR_EMAIL@example.com` | your email |
| README (project 1) | `YOUR_CONTENTHUB_REPO`, `YOUR_CONTENTHUB_DEMO_URL` | real repo / demo URLs (delete the demo link if none) |
| README (project 2) | `YOUR_SIGMAGPT_REPO`, `YOUR_SIGMAGPT_DEMO_URL` | real repo / demo URLs |
| README (SigmaGPT) | `TODO` comment | 2-3 features specific to SigmaGPT |
| Profile photo | placeholder in `about-photo.svg` | see step 3 |
| Project previews | placeholders | see step 3 |

## 3. Add your photo and screenshots
Put your images anywhere (e.g. `me.jpg`, `contenthub.png`, `sigmagpt.png`) and run:
```
python tools/build_assets.py --photo me.jpg --shot1 contenthub.png --shot2 sigmagpt.png
```
They are embedded into the retro window frames. Keep each image under ~500 KB.

## 4. Publish
1. On GitHub create a **public** repo named exactly your username (e.g. `krishna-sharma`).
2. Upload `README.md`, `assets/` (and optionally `tools/`).
3. Commit to `main`. The README now shows on your profile page.

## Notes
- Stats cards come from third-party services (github-readme-stats, streak-stats, activity-graph); they may be slow or rate-limited. Private contributions only show if enabled in your profile settings.
- GitHub can't use custom fonts or a page background, so all pixel text and the pink canvases are baked into SVGs.
- Testimonials were left out on purpose (no real ones provided).
