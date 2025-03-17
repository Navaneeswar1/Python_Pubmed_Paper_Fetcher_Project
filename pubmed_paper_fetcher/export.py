import csv
from typing import List, Dict, Any

def flatten_authors(authors: List[Dict[str, str]]) -> str:
    """Convert list of author dictionaries into a semicolon-separated string."""
    return "; ".join(author.get("Name", "N/A") for author in authors) if authors else "N/A"

def extract_doi(article_ids: List[Dict[str, str]]) -> str:
    """Extracts the DOI from the article IDs."""
    return next((aid["value"] for aid in article_ids if aid["idtype"] == "doi"), "N/A")

def export_to_csv(papers: List[Dict[str, Any]], filename: str) -> None:
    """Exports the filtered papers to a CSV file."""
    if not papers:
        print("⚠ No data to save.")
        return

    # Define CSV field names explicitly
    fieldnames = [
        "PubmedID", "Title", "PublicationDate", "Authors",
        "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"
    ]

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for paper in papers:
            writer.writerow({
                "PubmedID": paper.get("PubmedID", "N/A"),
                "Title": paper.get("Title", "N/A"),
                "PublicationDate": paper.get("PublicationDate", "N/A"),
                "Authors": flatten_authors(paper.get("Authors", [])),  # ✅ Convert authors to string
                "Non-academic Author(s)": paper.get("Non-academic Author(s)", "N/A"),
                "Company Affiliation(s)": paper.get("Company Affiliation(s)", "N/A"),
                "Corresponding Author Email": paper.get("Corresponding Author Email", "N/A"),
            })

    print(f"✅ Data saved to {filename}")
