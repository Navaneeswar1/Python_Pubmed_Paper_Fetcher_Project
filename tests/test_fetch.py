import pytest
from pubmed_paper_fetcher.fetch import fetch_paper_ids

def test_fetch_paper_ids():
    query = "antibiotics resistance"
    results = fetch_paper_ids(query, max_results=5)
    assert isinstance(results, list)
    assert len(results) > 0
    assert all(isinstance(p, str) for p in results)
