import re

salary_pattern = r"(\$\d{1,3}(,\d{3})*(\.\d{2})?|\d{1,3}(,\d{3})*(\.\d{2})?\s?[$£€])"


def format_salary(salary):
    if salary:
        return float(re.sub("[^0-9.]+", "", salary))
    return None


def parse_entry(entry):
    salary_list = re.findall(salary_pattern, entry["summary"])
    salary_min, salary_max = None, None
    if salary_list:
        salary_min = salary_list[0][0]
        if len(salary_list) > 1:
            salary_max = salary_list[1][0]
        salary_min, salary_max = format_salary(salary_min), format_salary(salary_max)

    description = entry["summary"].split("<br")[0]
    application_url = entry["link"].split("&from=rss")[0]

    title, company, location = entry["title"].rsplit("-", maxsplit=2)
    location_split = location.split(",")
    if len(location_split) > 1:
        city = location_split[0].strip()
        state = location_split[1].strip()
    else:
        city = location.strip()
        state = None

    return {
        "title": title.strip(),
        "company": company.strip(),
        "city": city,
        "state": state,
        "salary_min": salary_min,
        "salary_max": salary_max,
        "description": description,
        "application_url": application_url,
    }
