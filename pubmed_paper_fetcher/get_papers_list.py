import argparse
from pubmed_paper_fetcher.fetch import fetch_paper_ids, fetch_paper_details
from pubmed_paper_fetcher.filter import identify_non_academic_authors
from pubmed_paper_fetcher.export import export_to_csv
from pprint import pprint

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with industry-affiliated authors.")
    parser.add_argument("query", type=str, help="PubMed search query")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename", default="pubmed_results.csv")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    try:
        if args.debug:
            print(f"🔍 Debug: Searching for papers with query: {args.query}")

        paper_ids = fetch_paper_ids(args.query, debug=args.debug)
        if not paper_ids:
            print("⚠ No papers found for the given query.")
            return

        paper_details = fetch_paper_details(paper_ids, debug=args.debug)

        

        filtered_papers = identify_non_academic_authors(paper_details)
        if args.debug:
            print("\n📄 Final Papers Being Exported to CSV:")
            pprint(filtered_papers)

        if args.debug:
            print("\n🔍 Checking Author Affiliations in Fetch Results:")
            for paper in paper_details:
                print(f"🔹 {paper['Title']} ({paper['PubmedID']})")
                for author in paper['Authors']:
                    print(f"  - {author['Name']} | Affiliation: {author['Affiliation']}")

        if not filtered_papers:
            print("⚠ No papers matched the filtering criteria. Check author affiliations.")
            return

        export_to_csv(filtered_papers, args.file)
        print(f"✅ CSV file saved as {args.file}")

    except Exception as e:
        print(f"🚨 Error: {e}")

if __name__ == "__main__":
    main()
