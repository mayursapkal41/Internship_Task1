
This project focuses on cleaning and preprocessing a real-world dataset from Netflix, downloaded from [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows).

## 🧹 Task 1: Data Cleaning and Preprocessing

### ✅ Objective
To clean and prepare a raw dataset for analysis by handling:
- Missing values
- Duplicates
- Inconsistent text and date formats
- Column naming
- Data type mismatches

---

## 📦 Dataset Used
**File:** `netflix_titles.csv`  
**Source:** Kaggle - Netflix Movies and TV Shows Dataset

---

## 🛠️ Tools Used
- Python 🐍
- Pandas 📊

---

## 🧪 Cleaning Steps Performed

1. **Loaded the raw CSV file** using `pandas.read_csv()`.
2. **Handled missing values**:
   - Dropped rows with missing `title` or `type`.
   - Filled missing values in `director`, `cast`, `country`, `rating`, and `duration` with placeholders.
3. **Removed duplicate rows** using `drop_duplicates()`.
4. **Standardized text values**:
   - Trimmed spaces and corrected case for `country`, `type`, and `rating`.
5. **Formatted `date_added`** column to `dd-mm-yyyy` using `pd.to_datetime()` and `strftime()`.
6. **Renamed column headers** to be:
   - Lowercase
   - Underscore-separated (e.g., `date_added`)
7. **Saved the cleaned dataset** to `netflix_titles_cleaned.csv`.

---

## 💻 How to Run

```bash
# Step 1: Install pandas if not already installed
pip install pandas

# Step 2: Run the Python script
python clean_netflix_dataset.py
