# Amazon Review Semantic Search  🚀

Course / Semester • Due **1 Aug 2025**

A mini-research project that builds three retrieval systems over the Amazon
product-review corpus and evaluates them on aspect–sentiment queries.

---

## 0. Quick start (60 sec)

```bash
git clone https://github.com/your-handle/amazon-semantic-search.git
cd amazon-semantic-search
bash scripts/setup_env.sh        # creates venv + installs deps
bash scripts/download_dataset.sh # pulls the small review slice used in grading
python experiments/run_baseline.py --query "audio quality poor"