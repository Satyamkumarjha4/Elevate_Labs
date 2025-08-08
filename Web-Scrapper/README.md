# Web Scraper for News Headlines

A Python-based web scraper that automatically extracts news headlines from websites and saves them to a text file. Built with requests and BeautifulSoup for reliable web scraping with error handling and colorful terminal output.

## 📋 Project Overview

This is a Python web scraping application designed to extract news headlines from websites. The scraper uses the `requests` library to fetch web content and `BeautifulSoup` to parse HTML elements. It features automatic data collection, duplicate removal, file management, and a user-friendly colored terminal interface.

## ✨ Features

### Core Functionality
- **Web Scraping**: Fetch HTML content from news websites
- **HTML Parsing**: Extract headlines using CSS class selectors
- **Data Processing**: Clean and deduplicate scraped content
- **File Export**: Save headlines to formatted text files
- **Error Handling**: Robust error management for network and parsing issues

### Advanced Features
- **Configurable Targets**: Customizable URL and CSS class parameters
- **Duplicate Removal**: Automatic elimination of duplicate headlines
- **Timeout Protection**: Network request timeout for reliability
- **Colored Output**: Enhanced terminal experience with status indicators
- **Automatic Directory Creation**: Creates output directories as needed
- **UTF-8 Encoding**: Proper handling of international characters

### Visual Status Indicators
- 🔵 Blue (Cyan) - Processing information
- 🟢 Green - Success messages
- 🟡 Yellow - Warnings and notices
- 🔴 Red - Error messages

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- Required Python packages:
  - `requests` - For HTTP requests
  - `beautifulsoup4` - For HTML parsing
  - `colorama` - For colored terminal output

### Installation

1. Clone or download the repository:
   ```bash
   git clone <repository-url>
   cd Web-Scrapper
   ```

2. Install required dependencies:
   ```bash
   pip install requests beautifulsoup4 colorama
   ```

   Or use the requirements file if available:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Navigate to the Web-Scrapper directory and run:

```bash
python scrapper.py
```

## 📖 Usage

### Basic Usage

The scraper is pre-configured to work with a default news website:

```python
scraper = NewsScraper()
scraper.run()
```

### Custom Configuration

You can customize the scraper for different websites:

```python
scraper = NewsScraper(
    url='https://example-news-site.com',
    class_name='headline-class',
    filename='custom_headlines.txt'
)
scraper.run()
```

### Parameters

- **url**: Target website URL (default: 'https://thrivenews.co')
- **class_name**: CSS class name to search for headlines (default: 'p-url')
- **filename**: Output file path (default: 'Web-Scraper/headlines.txt')

### Example Output

The scraper will display colored status messages:

```
Fetching headlines from https://thrivenews.co with class 'p-url'...
Successfully scraped 15 headlines.
Saved 15 formatted headlines to 'Web-Scrapper/headlines.txt'.
```

### Output File Format

Headlines are saved in a formatted text file:

```
📰 Scraped Headlines from https://thrivenews.co
--------------------------------------------------
1. Breaking News: Major Technology Breakthrough
2. Sports Update: Championship Results
3. Weather Alert: Storm Warning Issued
...
```

## 🏗️ Code Architecture

### `NewsScraper` Class

#### Attributes
- `url`: Target website URL
- `class_name`: CSS class selector for headlines
- `filename`: Output file path
- `headlines`: List to store scraped headlines

#### Methods

##### `__init__(self, url=None, class_name='p-url', filename='Web-Scraper/headlines.txt')`
- Initialize scraper with configuration parameters
- Sets default values for all parameters

##### `fetch_headlines(self)`
- Sends HTTP GET request to target URL
- Parses HTML using BeautifulSoup
- Extracts text from elements with specified class
- Removes duplicates and empty content
- Handles network and parsing errors

##### `save_headlines(self)`
- Creates output directory if needed
- Writes formatted headlines to text file
- Handles file I/O errors
- Uses UTF-8 encoding for international characters

##### `run(self)`
- Executes the complete scraping workflow
- Calls fetch_headlines() followed by save_headlines()

### File Structure

```
Web-Scrapper/
├── scrapper.py         # Main application file
├── headlines.txt       # Output file (auto-created)
├── requirements.txt    # Dependencies (optional)
└── README.md          # This documentation
```

## 🛡️ Error Handling

The application includes comprehensive error handling for:

### Network Errors
- **Connection Timeouts**: 10-second timeout protection
- **HTTP Errors**: Status code validation with `raise_for_status()`
- **DNS Resolution**: Network connectivity issues
- **SSL/TLS Errors**: Certificate and encryption problems

### Parsing Errors
- **Invalid HTML**: Malformed document handling
- **Missing Elements**: Graceful handling when target class not found
- **Encoding Issues**: UTF-8 support for international content

### File System Errors
- **Directory Creation**: Automatic parent directory creation
- **Permission Errors**: Write permission validation
- **Disk Space**: File writing error handling

## 🔧 Technical Details

### Dependencies

```python
import os                    # File system operations
import requests             # HTTP requests
from bs4 import BeautifulSoup  # HTML parsing
from colorama import init, Fore, Style  # Colored output
from requests.exceptions import RequestException  # Error handling
```

### Key Features

- **HTTP Timeout**: 10-second request timeout
- **Duplicate Removal**: Uses `dict.fromkeys()` for order-preserving deduplication
- **Text Cleaning**: `get_text(strip=True)` for clean content extraction
- **Error Categorization**: Separate handling for network vs. parsing errors

### Data Processing

1. **Fetch**: HTTP GET request to target URL
2. **Parse**: BeautifulSoup HTML parsing
3. **Extract**: Find elements by CSS class
4. **Clean**: Strip whitespace and remove empty content
5. **Deduplicate**: Remove duplicate headlines
6. **Format**: Add numbering and headers
7. **Save**: Write to UTF-8 encoded text file

## 📁 Output Management

### File Creation
- Automatic directory creation using `os.makedirs()`
- UTF-8 encoding for international character support
- Formatted output with headers and numbering

### File Format
```
📰 Scraped Headlines from [URL]
--------------------------------------------------
1. [First Headline]
2. [Second Headline]
...
```

## ⚙️ Customization

### Different Websites

To scrape different news websites, modify the configuration:

```python
# Example for different news sites
scraper = NewsScraper(
    url='https://news.ycombinator.com',
    class_name='storylink',
    filename='hackernews_headlines.txt'
)
```

### Different CSS Selectors

Common CSS selectors for headlines:
- `h1`, `h2`, `h3` - Header tags
- `article-title` - Article title classes
- `headline` - Headline classes
- `title` - Generic title classes

### Multiple Sources

You can create multiple scraper instances for different sources:

```python
sources = [
    {'url': 'https://site1.com', 'class': 'headline', 'file': 'site1.txt'},
    {'url': 'https://site2.com', 'class': 'title', 'file': 'site2.txt'},
]

for source in sources:
    scraper = NewsScraper(
        url=source['url'],
        class_name=source['class'],
        filename=source['file']
    )
    scraper.run()
```

## 🚀 Future Enhancements

Potential improvements for the application:

### Features
- **Multiple CSS Selectors**: Support for fallback selectors
- **Data Validation**: Content quality checks
- **Scheduling**: Automated periodic scraping
- **Database Storage**: SQLite or other database backends
- **RSS Feed Support**: Alternative to HTML scraping
- **Content Filtering**: Keyword-based filtering

### Technical Improvements
- **Async Scraping**: Concurrent requests for multiple sites
- **Rate Limiting**: Respectful scraping with delays
- **User Agent Rotation**: Avoid detection
- **Proxy Support**: IP rotation capabilities
- **Caching**: Avoid duplicate requests

### Output Formats
- **JSON Export**: Structured data format
- **CSV Export**: Spreadsheet compatibility
- **XML Export**: Alternative structured format
- **Email Reports**: Automated delivery

## 📋 Best Practices

### Ethical Scraping
- **Respect robots.txt**: Check website scraping policies
- **Rate Limiting**: Don't overwhelm servers with requests
- **Terms of Service**: Comply with website terms
- **Attribution**: Credit data sources appropriately

### Technical Best Practices
- **Error Handling**: Always handle network and parsing errors
- **Timeouts**: Use reasonable request timeouts
- **Encoding**: Handle UTF-8 and other character encodings
- **Validation**: Verify data quality and completeness

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements such as:
- Additional news source support
- Enhanced error handling
- Performance optimizations
- New output formats
- Scheduling capabilities
- GUI interface

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

Created as part of the Elevate Labs development exercises.

## 🐛 Troubleshooting

### Common Issues

1. **Module not found errors**:
   ```bash
   pip install requests beautifulsoup4 colorama
   ```

2. **No headlines found**:
   - Check if the CSS class name is correct
   - Verify the website structure hasn't changed
   - Try different CSS selectors

3. **Network timeout errors**:
   - Check internet connectivity
   - Try increasing timeout value
   - Verify the target URL is accessible

4. **Permission denied (file writing)**:
   - Ensure write permissions in the output directory
   - Check disk space availability

5. **Encoding errors**:
   - The scraper uses UTF-8 encoding by default
   - Most international characters should work correctly

### Debugging Tips

- Use browser developer tools to inspect HTML structure
- Test CSS selectors in browser console
- Add print statements to debug data extraction
- Check network tab for request/response details

---

**Note**: This web scraper is designed for educational purposes. Always respect website terms of service and implement appropriate rate limiting for production use.