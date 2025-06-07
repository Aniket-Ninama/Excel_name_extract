
# Excel_name_project

A fast and efficient Python script that processes Excel files containing email addresses and generates a new Excel file with extracted first names. Perfect for cleaning and organizing email lists.

## 📦 Installation

First, clone the repository and install the required packages:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. Make sure your Excel file contains a column named **Email** with only email addresses.
2. Open a Python console or run the script with the path to your Excel file as input.

### Example:

```python
from excel_name_project import process_excel  # Assuming your main function is named process_excel

process_excel("path/to/your/input_file.xlsx")
```

## 📄 Output

The script will generate a new Excel file named **email.xlsx** in the same directory.  
This file will contain two columns:

- **First Name** — extracted from the email prefix
- **Email** — the original email address

## ✅ Example Input:

| Email                  |
|------------------------|
| johndoe@example.com    |
| janesmith@example.com  |

## ✅ Example Output:

| First Name | Email                  |
|------------|------------------------|
| John       | johndoe@example.com    |
| Jane      | jane.smith@example.com  |

---

Use for quick email processing.
