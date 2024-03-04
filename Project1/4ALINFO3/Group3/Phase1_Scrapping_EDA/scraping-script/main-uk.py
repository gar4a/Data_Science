from jobspy import scrape_jobs  # Assuming jobspy is a library for job scraping
import pandas as pd
import time
import datetime
 
# Job titles (list of strings)
job_titles = [
    "Software Developer",
    "Software Engineer",
    "Systems Analyst",
    "Database Administrator",
    "System Administrator",
    "Network Engineer",
    "Network Administrator",
    "Cybersecurity Analyst",
    "Cybersecurity Engineer",
    "Software Quality Assurance Specialist",
    "Solution Architect",
    "AI Business Analyst",
    "Mobile App Developer",
    "Machine Learning Analyst",
    "Data Analyst",
    "Machine Learning Engineer",
    "Web Developer",
    "Business Intelligence Analyst",
    "Systems Performance Analyst",
    "Operations Analyst",
    "Cloud Systems Administrator",
    "DevOps Developer",
    "Cloud Architect",
    "DevOps Engineer",
    "Robotic Process Automation (RPA) Specialist",
    "Knowledge Management Analyst",
    "IT Consultant",
    "Augmented_Virtual Reality Analyst",
    "Server Administrator",
    "Test Automation Analyst",
]
 
locations = [
    "Liverpool, LIV",
    "Dundee, DND",
    "Wrexham, WRX"
    "Newtownabbey, NTB",
    "Leicester, LEI",
    "Kilmarnock, KMK",
    "Derbey, DER",
    "Bradford, BRD",
    "Llanelli, LLA",
    "Newtownards, NTA"
]
 
# Constants
results_wanted = 1000
max_retries = 1
results_in_each_iteration = 30
 
# Loop through job titles and locations
for job_title in job_titles:
    for location in locations:
        all_jobs = []
        offset = 0
        while len(all_jobs) < results_wanted:
            retry_count = 0
            jobs_found_in_iteration = False  # Track if jobs are found in the current iteration
 
            while retry_count < max_retries and not jobs_found_in_iteration:
                print(f"Scraping from {offset} to {offset + results_in_each_iteration} jobs for {job_title} in {location}")
                try:
                    jobs = scrape_jobs(
                        site_name=["indeed", "linkedin", "zip_recruiter"],
                        search_term=job_title,
                        location=location,
                        results_wanted=min(results_in_each_iteration, results_wanted - len(all_jobs)),
                        country_indeed="UK",
                        offset=offset
                    )
 
                    if not jobs.empty:
                        all_jobs.extend(jobs.to_dict('records'))
                        jobs_found_in_iteration = True  # Update flag when jobs are found
                        offset += len(jobs)  # Update offset based on actual jobs found
                        print(f"Scraped from {offset - len(jobs)} to {offset} jobs for {job_title} in {location}")
                    else:
                        print(f"No more jobs found for {job_title} in {location} at offset {offset}. Moving to next location.")
                        break  # Exit loop if no jobs are found in the current attempt
 
                    time.sleep(10)  # Delay to avoid rate limiting
 
                except Exception as e:
                    print(f"Error: {e}")
                    retry_count += 1
                    if retry_count >= max_retries:
                        print(f"Max retries reached for {job_title} in {location}. Moving to next location.")
                        break
                    time.sleep(10 * retry_count)  # Incremental backoff
 
            if not jobs_found_in_iteration:
                break  # Break the while loop if no jobs found after retries
 
        if all_jobs:
            # Save the collected job data
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"job_data_uk/{job_title.replace(' ', '_')}_{location.replace(', ', '_')}_{timestamp}.csv"
            jobs_df = pd.DataFrame(all_jobs)
            jobs_df.to_csv(filename, index=False)
            print(f"Saved {len(all_jobs)} jobs for {job_title} in {location} to {filename}")
 
print("Completed scraping for all job titles.")