from pubmed_paper_fetcher.filter import identify_non_academic_authors

def test_identify_non_academic_authors():
    sample_papers = [
        {
            "PubmedID": "12345",
            "Title": "A Study on Pharma Research",
            "Publication Date": "2023-01-01",
            "Authors": [{"name": "Dr. John Doe", "affiliation": "XYZ Biotech Inc"}]
        }
    ]

    result = identify_non_academic_authors(sample_papers)
    assert len(result) > 0
    assert "Non-academic Author(s)" in result[0]
    assert "Company Affiliation(s)" in result[0]
