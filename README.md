# KFL Repository

Welcome to the Fantasy Football Repository! This repository contains code for managing fantasy football matchups and generating formatted scores for analysis. Below, you will find information on how to use the code, dependencies, and other relevant details.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [License](#license)

## Prerequisites

Before you get started, make sure you have the following installed on your system:

- Python 3.11
- Pip (Python package manager)

## Installation

To set up the fantasy football project, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   cd fantasy-football-repo
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root directory and add your OpenAI API key and sleeper league id in the following format:

   ```
   OPENAI_API_KEY=your-api-key-goes-here
   LEAGUE_ID=your-league-id-goes-here
   ```

## Usage

To use the fantasy football code, run the following command in the terminal or command prompt:

```bash
python main.py -w <week-number>
```

Replace `<week-number>` with the desired week for which you want to generate fantasy football scores and matchups.

## How It Works

This codebase fetches fantasy football matchups for a specific week using the Sleeper API. It calculates scores and formats the data into a tabular format, which can be easily copied into Excel or other spreadsheet tools for further analysis.

The main components of the code are as follows:

- **`main.py`**: This script contains the main functionality. It retrieves matchups for the specified week, calculates scores, and formats the data.

- **`sleeper_wrapper`**: This is a Python wrapper for the Sleeper API, used to fetch fantasy football league data.

- **`openai`**: This module integrates OpenAI's GPT-3.5 Turbo model to format the data into a user-friendly format.

- **`.env`**: This configuration file stores the OpenAI API key. Make sure to keep it secure and never share it publicly.

## License

This project is licensed under the [MIT License](LICENSE), which means you are free to use, modify, and distribute the code as you like. See the [LICENSE](LICENSE) file for more details.