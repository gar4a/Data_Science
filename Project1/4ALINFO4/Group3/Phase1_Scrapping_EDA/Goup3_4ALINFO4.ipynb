from bs4 import BeautifulSoup
import pandas as pd
from google.colab import drive
import requests

# Mount Google Drive
drive.mount("/content/gdrive")
html_file_path = "/content/gdrive/My Drive/Data_Science_Project_2024/sample.html"

url = "https://radhwene-05.github.io/fakejobs/"

# Fetch HTML content from the URL
response = requests.get(url)
html_content = response.text

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Extract job offer details
job_offers = []
job_id_counter = 1  # Counter for assigning unique job IDs

for job_card in soup.find_all("div", class_="column is-half"):
    # Assign a unique job ID
    job_id = job_card.find("div", class_="card").attrs.get(
        "id", f"job-{job_id_counter}"
    )
    job_id = int(job_id.split("-")[-1])
    job_id_counter += 1

    # Check if the job title or description mentions remote work or telecommuting
    title = job_card.find("h2", class_="title is-5").text.strip()
    description = (
        job_card.find("p", class_="has-text-weight-bold", text="Description:")
        .find_next_sibling("p")
        .text.strip()
    )
    requirements = (
        job_card.find("p", class_="has-text-weight-bold", text="Requirements:")
        .find_next_sibling("p")
        .text.strip()
    )
    benefits = (
        job_card.find("p", class_="has-text-weight-bold", text="Benefits:")
        .find_next_sibling("p")
        .text.strip()
    )

    telecommuting = (
        "home" in title.lower()
        or "remote" in title.lower()
        or "home" in description.lower()
        or "remote" in description.lower()
        or "home" in benefits.lower()
        or "remote" in benefits.lower()
        or "home" in requirements.lower()
        or "remote" in requirements.lower()
    )

    # Extract logo URL
    logo_url_tag = job_card.find("figure", class_="image is-48x48").find("img")
    logo_url = logo_url_tag["src"] if logo_url_tag else ""

    # Extract Has Questions information
    has_questions_tag = job_card.find(
        "p", class_="has-text-weight-bold", text="Has Questions"
    )
    has_questions_value = 0  # Default to 0 if not found
    if has_questions_tag:
        next_sibling = has_questions_tag.find_next_sibling("p")
        if next_sibling and next_sibling.text.strip().isdigit():
            has_questions_value = int(next_sibling.text.strip())

    # Create job details dictionary
    job_details = {
        "JobID": job_id,
        "Title": title,
        "Location": job_card.find("p", class_="location").text.strip(),
        "Department": job_card.find(
            "p", class_="has-text-weight-bold", text="Department:"
        )
        .find_next_sibling("p")
        .text.strip(),
        "SalaryRange": job_card.find(
            "p", class_="has-text-weight-bold", text="Salary Range:"
        )
        .find_next_sibling("p")
        .text.strip(),
        "CompanyProfile": job_card.find(
            "p", class_="has-text-weight-bold", text="Company Profile:"
        )
        .find_next_sibling("p")
        .text.strip(),
        "Description": description,
        "Requirements": job_card.find(
            "p", class_="has-text-weight-bold", text="Requirements:"
        )
        .find_next_sibling("p")
        .text.strip(),
        "Benefits": job_card.find("p", class_="has-text-weight-bold", text="Benefits:")
        .find_next_sibling("p")
        .text.strip(),
        "Telecommuting": telecommuting,
        "HasCompanyLogo": int(bool(logo_url)),  # Check if logo URL is present
        "LogoURL": logo_url,  # Include logo URL in the data
        "HasQuestions": has_questions_value,
        "EmploymentType": job_card.find(
            "p", class_="has-text-weight-bold", text="Employment Type:"
        )
        .find_next_sibling("p")
        .text.strip(),
        "RequiredExperience": job_card.find(
            "p", class_="has-text-weight-bold", text="Required Experience:"
        )
        .find_next_sibling("p")
        .text.strip(),
        "RequiredEducation": 1
        if job_card.find("p", class_="has-text-weight-bold", text="Requirements:")
        .find_next_sibling("p")
        .text.strip()
        .startswith("Education:")
        else 0,
        "Industry": job_card.find("p", class_="has-text-weight-bold", text="Industry:")
        .find_next_sibling("p")
        .text.strip(),
        "ScreeningQuestions": 0,  # Default value for screening questions
    }

    # Check if the "Screening Questions" section is found
    screening_questions_tag = job_card.find(
        "p", class_="has-text-weight-bold", text="Screening Questions:"
    )
    if screening_questions_tag:
        # Find the unordered list (ul) containing screening questions
        screening_questions_ul = screening_questions_tag.find_next("ul")
        if screening_questions_ul:
            # Extract screening questions from list items (li)
            screening_questions = [
                li.text.strip() for li in screening_questions_ul.find_all("li")
            ]
            job_details["ScreeningQuestions"] = 1 if screening_questions else 0

    # Append job details to the list
    job_offers.append(job_details)

# Convert the extracted data to a DataFrame
df = pd.DataFrame(job_offers)

# Save the DataFrame to a CSV file
csv_file_path = (
    "/content/gdrive/My Drive/Data_Science_Project_2024/Group3_job_offers_dataset.csv"
)
df.to_csv(csv_file_path, index=False)

print("CSV file created successfully at:", csv_file_path)
