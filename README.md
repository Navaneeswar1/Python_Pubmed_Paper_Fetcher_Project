# PubMed Paper Fetcher

## Overview

This Python program fetches research papers from PubMed based on a user-specified query, filters papers where at least one author is affiliated with a pharmaceutical or biotech company, and exports the results as a CSV file.



## Installation

## Prerequisites----->

Python 3.8+

Poetry (for dependency management)

### Install Poetry

```sh
pip install poetry
```

## Setup

Clone the repository----->

```sh
git clone https://github.com/yourusername/pubmed_paper_fetcher.git
cd pubmed_paper_fetcher
```

Install dependencies:

```sh
poetry install
```

## Usage

## Run the program

Execute the script with a search query to fetch papers:

```sh
poetry run python get_papers_list.py "antimicrobial resistance"
```

Options:

-f, --file <filename> : Specify output CSV filename (default: pubmed_results.csv)
-d, --debug : Enable debug mode
Example:

```sh
poetry run python get_papers_list.py "cancer research" -f output.csv -d
```

## Tools & Libraries Used

Entrez API (BioPython) – Fetches PubMed papers. 
Poetry – Manages dependencies. 
argparse – Parses command-line arguments. 
mypy (optional) – Static type checking. 

## Contributing

Feel free to open issues or submit pull requests.

## License

MIT License
