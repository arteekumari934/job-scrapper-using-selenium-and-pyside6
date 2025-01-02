
![Capture1](https://github.com/user-attachments/assets/59d29e86-a0ba-4d5c-a113-07833e55bb9f)




# Job Scraper - Naukri

This project is a **desktop application** built with Python and PySide6 for scraping job postings from **Naukri.com**. It allows users to search for jobs based on location, experience, and skills, and displays the results in a user-friendly table.

---

## Features

1. **User-Friendly Interface**
   - Filters for location, experience, and skills.
   - Interactive table to display job results.

2. **Web Scraping**
   - Scrapes job details from **Naukri.com** using Selenium.
   - Runs in **headless mode** for efficient scraping.

3. **Dynamic Search**
   - Fetches job details such as title, company, experience, location, skills, and job links.
   - Results are displayed in a structured table.

4. **Action Buttons**
   - **Search**: Fetch job postings based on filters.
   - **Clear**: Reset the results table.

---

## Technologies Used

- **Python**  
  Libraries:  
  - [PySide6](https://doc.qt.io/qtforpython/)
  - [Selenium](https://www.selenium.dev/)

- **Naukri.com** as the source for job postings.

---

## Requirements

1. Python 3.7 or later
2. Required Python Libraries:
   ```bash
   pip install PySide6 selenium
ChromeDriver:
Download ChromeDriver compatible with your Chrome browser version from here.
Update the Service path in the script:
python
Copy code
service = Service(r"path_to_chromedriver")
How to Run
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/job-scraper.git
cd job-scraper
Install the required dependencies:

bash
Copy code
pip install PySide6 selenium
Update the ChromeDriver path in the script:

python
Copy code
service = Service(r"C:/path/to/chromedriver.exe")
Run the application:

bash
Copy code
python main.py
