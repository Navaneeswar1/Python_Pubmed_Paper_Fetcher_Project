import requests
import json
from typing import List, Dict, Optional
from xml.etree import ElementTree as ET

DEBUG = True  # Set to False in production

def fetch_paper_ids(query: str, max_results: int = 10, debug: bool = DEBUG) -> List[str]:
    """Fetch PubMed paper IDs for a given query."""
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors

        data = response.json()
        if debug:
            print("🔍 PubMed API Response (fetch_paper_ids):")
            print(json.dumps(data, indent=2))  # Pretty-print JSON response

        return data.get("esearchresult", {}).get("idlist", [])

    except requests.exceptions.RequestException as req_err:
        print(f"🚨 Network Error: {req_err}")
    except json.JSONDecodeError:
        print(f"🚨 Error: Unable to parse JSON response from PubMed API.")
    except Exception as e:
        print(f"🚨 Unexpected Error: {e}")

    return []


def fetch_paper_details(paper_ids: List[str], debug: bool = DEBUG) -> List[Dict[str, Optional[str]]]:
    """Fetch full paper details (title, authors, affiliations) from PubMed."""
    if not paper_ids:
        return []

    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "xml"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        root = ET.fromstring(response.text)

        papers = []
        for article in root.findall(".//PubmedArticle"):
            paper_id = article.find(".//PMID").text
            title = article.find(".//ArticleTitle").text if article.find(".//ArticleTitle") is not None else "N/A"
            pub_date = article.find(".//PubDate/Year")
            pub_date = pub_date.text if pub_date is not None else "N/A"

            authors = []
            for author in article.findall(".//Author"):
                last_name = author.findtext("LastName", "").strip()
                fore_name = author.findtext("ForeName", "").strip()
                name = f"{last_name} {fore_name}".strip()
                affiliation = author.findtext(".//Affiliation", "N/A")

                authors.append({"Name": name, "Affiliation": affiliation})

            papers.append({
                "PubmedID": paper_id,
                "Title": title,
                "PublicationDate": pub_date,
                "Authors": authors
            })

        if debug:
            print("📄 Full Paper Details (fetch_paper_details):")
            print(json.dumps(papers, indent=2))

        return papers

    except requests.exceptions.RequestException as req_err:
        print(f"🚨 Network Error: {req_err}")
    except json.JSONDecodeError:
        print(f"🚨 Error: Unable to parse JSON response from PubMed API.")
    except Exception as e:
        print(f"🚨 Unexpected Error: {e}")

    return []
