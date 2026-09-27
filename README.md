# Which Areas in Lagos are prone to flooding, along with pathways for routing flooded areas? (OJO LGA)

This project helps quickly identify areas prone to flooding, especially during the rainy season.
It also identifies the best drainage routes for flooded areas.
For the Urban Planning Committee.
Ojo LGA, Lagos State, Nigeria.

**GeoDev Lab Africa, Cohort One.** Yusuf Isaiah Ifeanyichukwu

---

## The question

Flooded areas in Ojo LGA with possible drainage routes.

## What's in here

```
<project-name>/
├── docs/
│   ├── 01-project-brief.md      Week 1
│   ├── 02-data-notes.md         Week 2
│   └── 03-data-preparation.md   Week 3
├── data/
│   ├── raw/                     downloads, not committed
│   └── processed/               outputs, not committed
├── scripts/
├── month-1/
│   ├── month-1-surmarry.md                  
│   └── waterway_extent          output map of month one
└── requirements.txt
```

## How to run it

```bash
git clone https://github.com/Isadragon18/geodev-lab-project.git
cd geodev-lab-project

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

The data is not in this repository. Every source is linked in
[the project brief](docs/01-project-brief.md), so anyone can fetch it.

## Progress

- [x] Week 1, project brief with a source link for every dataset
- [x] Week 2, data downloaded, opened, and described
- [x] Week 3, reprojected, clipped and quality-checked
- [x] Week 4, first spatial analysis, checked four ways

---

Yusuf Isaiah Ifeanyichukwu · GeoDev Lab Africa
Learn. Build. Collaborate. Transform.
