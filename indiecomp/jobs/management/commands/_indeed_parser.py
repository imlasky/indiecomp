import re

salary_range_regex = re.compile(r'\$\d+(,\d{3})*(\.\d{2})?\s*-\s*\$\d+(,\d{3})*(\.\d{2})?')

def format_salary(salary):
    return float(re.sub("[^0-9.]+", "", salary))

def parse_entry(entry):
    salary_range = salary_range_regex.search(entry['summary'])
    salary_min, salary_max = None, None
    if salary_range:
        salary_min, salary_max = salary_range.group(0).split('-')
        salary_min, salary_max = format_salary(salary_min), format_salary(salary_max)


    title, company, location = entry["title"].rsplit('-', maxsplit=2)
    return {
        "title": title.strip(),
        "company": company.strip(),
        "location": location.strip(),
        "salaryMin": salary_min,
        "salaryMax": salary_max,
    }