# Hacker News Web Scraper

Web scraping program that filters stories from the Hacker News homepage and extracts information about stories with 100 or more points from the first 5 pages.

## Disclaimer

The tools and scripts provided in this repository are made available for educational purposes only and are intended to be used for testing and protecting systems with the consent of the owners. The author does not take any responsibility for the misuse of these tools. It is the end user's responsibility to obey all applicable local, state, national, and international laws. The developers assume no liability and are not responsible for any misuse or damage caused by this program. Under no circumstances should this tool be used for malicious purposes. The author of this tool advocates for the responsible and ethical use of security tools. Please use this tool responsibly and ethically, ensuring that you have proper authorization before engaging any system with the techniques demonstrated by this project.

## Features

- **Web Scraping Multiple Pages:** Scrape content from the first five pages of the Hacker News website. This requires fetching each page's HTML content and parsing it to extract relevant data.
- **Filtering Stories Based on Points:** Filter out and aggregate stories that have 100 or more points. Inspect each story's point value and including only those meeting the points threshold in the final data set.
- **Data Extraction:** For each qualifying story, extract the title, URL, and points. Parse the HTML structure of the page, then locate and extract these data points.
- **Sorting the Extracted Data:** Extracted stories need to be sorted in descending order based on the number of points. This is done to prioritize stories with higher engagement or popularity.
- **Modular Code Design**: Separate functions handling specific parts of the process. This includes functions for fetching stories from a page, sorting stories by points, and aggregating stories across multiple pages.

## Prerequisites

- **Operating System**: Tested on Ubuntu 22.04.4 LTS but should be compatible with other Unix-like systems as well as Windows and macOS.
- **Python Version**: Python 3.7+
- `requests`: For making HTTP requests to the Hacker News website.
- `beautifulsoup4`: For parsing HTML and extracting data. Beautiful Soup is a Python library for pulling data out of HTML and XML files. It provides simple methods for navigating, searching, and modifying the parse tree.

## Installation

1. **Clone the repository**:
    
    ```bash
    git clone https://github.com/CyberWolfByte/hacker-news-web-scraper.git
    cd hacker-news-web-scraper
    ```
    
2. **Install dependencies**: You can install the required Python libraries using pip.
    
    ```bash
    pip install requests beautifulsoup4
    ```
    

## Usage

**Run the scraper**: The webscraper script can be executed directly from the command line.

```bash
python3 webscraper.py
```

## How It Works

- The function `get_top_hn_stories` is responsible for fetching stories from a given URL with 100 or more points.
- It parses the HTML to extract story titles, URLs, and points.
- The function `sort_stories_by_points` sorts the stories by their points in descending order.
- The function `stories_from_first_five_pages` aggregates stories from the first five pages of Hacker News.
- This modular approach makes the code organized and easier to maintain.
- This implementation ensures that only stories with 100+ points are considered, sorted in descending order of points.

## Contributing

If you have an idea for an improvement or if you're interested in collaborating, you are welcome to contribute. Please feel free to open an issue or submit a pull request.

## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.
