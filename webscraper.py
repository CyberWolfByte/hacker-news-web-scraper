import requests
from bs4 import BeautifulSoup


def get_top_hn_stories(url):
    """Fetch stories with 100+ points from a single Hacker News page URL."""
    # Send a GET request to the provided URL
    response = requests.get(url)
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    stories = []

    # Use CSS selector 'tr.athing' to find all story rows on the page
    story_rows = soup.select('tr.athing')
    for row in story_rows:
        # For each story, find the next sibling row which contains the score
        score_row = row.find_next_sibling('tr')
        score_tag = score_row.select_one('.score')  # Select the score tag

        # Check if score tag is found and extract the points
        if score_tag:
            points = int(score_tag.text.split()[0])  # Convert points text to an integer
            # Filter out stories with less than 100 points
            if points >= 100:
                title_tag = row.select_one('span.titleline')  # Select the title tag within the story row

                if title_tag:
                    # Extract the title text and the story URL
                    title = title_tag.text
                    story_url = title_tag.find('a')['href']
                    # Append the story details to the stories list
                    stories.append({'title': title, 'url': story_url, 'points': points})

    return stories


def sort_stories_by_points(stories):
    """Sort stories by points in descending order."""
    # Use sorted() function with a lambda as the key for sorting by points
    return sorted(stories, key=lambda x: x['points'], reverse=True)


def stories_from_first_five_pages():
    """Aggregate stories with 100+ points from the first five pages of Hacker News."""
    base_url = 'https://news.ycombinator.com/'
    all_stories = []

    # Iterate through the first five pages
    for page in range(1, 6):
        # Construct the URL for each page
        url = f"{base_url}?p={page}"
        # Extend the all_stories list with stories from each page
        all_stories.extend(get_top_hn_stories(url))

    return all_stories


# Fetch and sort stories from the first five pages
all_stories = stories_from_first_five_pages()
sorted_stories = sort_stories_by_points(all_stories)

# Print sorted stories
for story in sorted_stories:
    print(f"Title: {story['title']}")
    print(f"URL: {story['url']}")
    print(f"Points: {story['points']}")
    print()

# NOTE:
# - The function get_top_hn_stories is responsible for fetching stories from a given URL with 100 or more points.
# - It parses the HTML to extract story titles, URLs, and points.
# - The function sort_stories_by_points sorts the stories by their points in descending order.
# - The function stories_from_first_five_pages aggregates stories from the first five pages of Hacker News.
# - This modular approach makes the code organized and easier to maintain.
# - This implementation ensures that only stories with 100+ points are considered, sorted in descending order of points.
