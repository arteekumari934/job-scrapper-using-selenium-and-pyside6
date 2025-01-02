import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QWidget, QPushButton, QLabel, QLineEdit, QTableWidget, QTableWidgetItem,
    QComboBox
)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class JobScraperApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Job Scraper - Naukri")
        self.setGeometry(100, 100, 1000, 600)

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.layout = QVBoxLayout()

        self.setup_filters()
        self.setup_table()
        self.setup_actions()

        self.main_widget.setLayout(self.layout)

    def setup_filters(self):
        filter_layout = QHBoxLayout()

        # Location Filter
        self.location_input = QLineEdit()
        self.location_input.setPlaceholderText("Location")
        filter_layout.addWidget(QLabel("Location:"))
        filter_layout.addWidget(self.location_input)

        # Experience Filter
        self.experience_input = QLineEdit()
        self.experience_input.setPlaceholderText("Experience (e.g., 0-2 Yrs)")
        filter_layout.addWidget(QLabel("Experience:"))
        filter_layout.addWidget(self.experience_input)

        # Skills Filter
        self.skills_input = QLineEdit()
        self.skills_input.setPlaceholderText("Skills")
        filter_layout.addWidget(QLabel("Skills:"))
        filter_layout.addWidget(self.skills_input)

        self.layout.addLayout(filter_layout)

    def setup_table(self):
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["Title", "Company", "Experience", "Location", "Skills", "Website"])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.layout.addWidget(self.table)

    def setup_actions(self):
        action_layout = QHBoxLayout()

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_jobs)
        action_layout.addWidget(self.search_button)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_results)
        action_layout.addWidget(self.clear_button)

        self.layout.addLayout(action_layout)

    def search_jobs(self):
        location = self.location_input.text()
        experience = self.experience_input.text()
        skills = self.skills_input.text()

        jobs = self.scrape_jobs(location, experience, skills)
        self.populate_table(jobs)

    def clear_results(self):
        self.table.setRowCount(0)

    def scrape_jobs(self, location, experience, skills):
        chrome_options = Options()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")  # Running in headless mode

        service = Service(r"C:/Program Files/Google/Chrome/Application/chromedriver/chromedriver-win64/chromedriver.exe")  # Replace with your chromedriver path
        driver = webdriver.Chrome(service=service, options=chrome_options)

        try:
            print("Opening the Naukri job search page...")
            # Construct the URL with filters
            search_url = f"https://www.naukri.com/software-developer-jobs-in-bengaluru?k=software%20developer&l={location}&experience={experience}"
            driver.get(search_url)

            # Wait for job elements to load
            job_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//article[contains(@class, 'jobTuple')]"))
            )

            # Collect job details
            jobs = self.collect_jobs(driver, job_elements)

            return jobs

        except Exception as e:
            print(f"Error occurred while scraping jobs: {e}")
            return []

        finally:
            driver.quit()

    def collect_jobs(self, driver, job_elements):
        jobs = []
        for job_element in job_elements:
            try:
                title = job_element.find_element(By.XPATH, ".//a[@class='title']").text
            except:
                title = "N/A"
            try:
                company = job_element.find_element(By.XPATH, ".//a[@class='comp-name']").text
            except:
                company = "N/A"
            try:
                experience = job_element.find_element(By.XPATH, ".//span[@class='expwdth']").text
            except:
                experience = "N/A"
            try:
                location = job_element.find_element(By.XPATH, ".//span[@class='locWdth']").text
            except:
                location = "N/A"
            try:
                skills = job_element.find_element(By.XPATH, ".//ul[@class='tags-gt']").text
            except:
                skills = "N/A"
            try:
                website = job_element.find_element(By.XPATH, ".//a[@class='title']").get_attribute("href")
            except:
                website = "N/A"

            jobs.append({
                "title": title,
                "company": company,
                "experience": experience,
                "location": location,
                "skills": skills,
                "website": website
            })

        return jobs

    def populate_table(self, jobs):
        self.table.setRowCount(len(jobs))
        for row, job in enumerate(jobs):
            self.table.setItem(row, 0, QTableWidgetItem(job["title"]))
            self.table.setItem(row, 1, QTableWidgetItem(job["company"]))
            self.table.setItem(row, 2, QTableWidgetItem(job["experience"]))
            self.table.setItem(row, 3, QTableWidgetItem(job["location"]))
            self.table.setItem(row, 4, QTableWidgetItem(job["skills"]))
            self.table.setItem(row, 5, QTableWidgetItem(job["website"]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JobScraperApp()
    window.show()
    sys.exit(app.exec())
