import requests

def get_cve_details(cve_id: str):
    # Official NVD REST API v2 Endpoint
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve_id}"
    
    headers = {
        "User-Agent": "SecurityChecker/1.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        vulnerabilities = data.get("vulnerabilities", [])
        if not vulnerabilities:
            return f"No records found for {cve_id}."

        cve_data = vulnerabilities[0]["cve"]
        
        # Extract key information
        description = cve_data["descriptions"][0]["value"]
        published_date = cve_data["published"]
        
        # Extract CVSS v3 Severity Score if available
        cvss_score = "N/A"
        metrics = cve_data.get("metrics", {})
        if "cvssMetricV31" in metrics:
            cvss_score = metrics["cvssMetricV31"][0]["cvssData"]["baseScore"]
        elif "cvssMetricV30" in metrics:
            cvss_score = metrics["cvssMetricV30"][0]["cvssData"]["baseScore"]

        return {
            "CVE ID": cve_id,
            "CVSS Score": cvss_score,
            "Published": published_date,
            "Description": description
        }

    except requests.exceptions.RequestException as e:
        return f"Error fetching CVE data: {e}"

# Example Usage
if __name__ == "__main__":
    result = get_cve_details("CVE-2021-44228")  # Log4Shell
    print(result)
