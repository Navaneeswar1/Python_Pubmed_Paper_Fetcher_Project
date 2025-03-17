import argparse
import sys
from pprint import pprint
from pubmed_paper_fetcher.fetch import fetch_paper_ids, fetch_paper_details
from pubmed_paper_fetcher.filter import identify_non_academic_authors
from pubmed_paper_fetcher.export import export_to_csv

def main():
    parser = argparse.ArgumentParser(
        description="Fetch PubMed papers with at least one industry-affiliated author."
    )
    parser.add_argument("query", type=str, help="PubMed search query")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()

    try:
        if args.debug:
            print(f"🔍 Searching for: {args.query}")

        paper_ids = fetch_paper_ids(args.query)
        if args.debug:
            print(f"📄 Fetched Paper IDs: {paper_ids}")

        paper_details = fetch_paper_details(paper_ids)
        if args.debug:
            print(f"📑 Paper Details:\n{paper_details}")

        filtered_papers = identify_non_academic_authors(paper_details)
        if args.debug:
            print(f"🛑 Filtered Papers:\n{filtered_papers}")

        if args.file:
            export_to_csv(filtered_papers, args.file)
            print(f"✅ Results saved to {args.file}")
        else:
            pprint(filtered_papers)

    except Exception as e:
        print(f"🚨 Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
