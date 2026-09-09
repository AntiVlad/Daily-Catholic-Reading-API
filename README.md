# Daily Catholic Reading API

A lightweight Flask microservice that dynamically scrapes and delivers the daily Catholic Mass readings (First Reading, Responsorial Psalm, Second Reading, Alleluia, and Gospel) in structured JSON format.

## Features

- **Automated Web Scraping**: Parses daily liturgical readings from Catholic Gallery using BeautifulSoup.
- **RESTful JSON Endpoint**: Serves clean, parsed text for each liturgical reading part.
- **Timezone Awareness**: Handles UTC/GMT+1 liturgical date formatting automatically.

---

## Prerequisites

- [Python](https://www.python.org/) (v3.8 or higher)
- pip

---

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AntiVlad/Daily-Catholic-Reading-API.git
   cd Daily-Catholic-Reading-API
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the API server**:
   ```bash
   python reading.py
   ```

The server will start on `http://localhost:3000` (or `http://localhost:5000`).

---

## API Reference

### Get Today's Mass Readings

**Endpoint**: `GET /daily-readings`

**Response Example**:
```json
[
  "FIRST READING ...",
  "RESPONSORIAL PSALM ...",
  "SECOND READING ...",
  "ALLELUIA ...",
  "GOSPEL ..."
]
```

---

## License

This project is open source and available under the MIT License.
