from typing import List, Dict

NON_ACADEMIC_KEYWORDS = [
    "pharma", "biotech", "corporation", "inc", "ltd", "gmbh", "s.a.", "pvt", "llc",
    "industries", "laboratories", "bioscience", "therapeutics", "lifesciences", "research institute"
]


def identify_non_academic_authors(papers: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Filters papers where at least one author is affiliated with a pharmaceutical or biotech company."""
    filtered_papers = []

    for paper in papers:
        non_academic_authors = []
        company_affiliations = []

        for author in paper.get("Authors", []):
            # Handle different possible keys for affiliation
            affiliation = author.get("Affiliation", "") or ", ".join(author.get("Affiliations", [])) or ""

            # Convert to lowercase for case-insensitive matching
            affiliation_lower = affiliation.lower()

            # Debugging: Print each affiliation being checked
            print(f"🔍 Checking Affiliation: {affiliation}")

            if any(keyword in affiliation_lower for keyword in NON_ACADEMIC_KEYWORDS):
                non_academic_authors.append(author.get("Name", "Unknown Author"))
                company_affiliations.append(affiliation)

        if non_academic_authors:
            paper["Non-academic Author(s)"] = "; ".join(non_academic_authors)
            paper["Company Affiliation(s)"] = "; ".join(company_affiliations)
            filtered_papers.append(paper)

    return filtered_papers
