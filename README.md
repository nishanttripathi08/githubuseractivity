# GitHub User Activity CLI
A simple command-line application that uses the GitHub API to fetch and display a user's recent GitHub Activity

### Features
+ Fetches a GitHub user's recent activity
+ Displays activity in the terminal
+ Supports multiple GitHub event types
+ Displays different actions for issues, comments, and pull requests
+ Handles invalid usernames and server errors
+ Uses the GitHub REST API

### Supported Events
+ Push events
+ Issue events
+ Issue comment events
+ Pull request events
+ Create events
+ Delete events

### Requirements 
+ Python 3.10+
+ Internet connection
+ No external libraries required

### How to Run
Run the program with a GitHub username
```bash
python3 main.py nishanttripathi08
```

### Example Output:
```bash
Pushed commits to nishanttripathi08/githubuseractivity
Opened a new issue in nishanttripathi/githubuseractivity
Created comment on nishanttripathi/githubuseractivity
Opened a pull request in nishanttripathi/githubuseractivity
Created a branch in nishanttripathi/githubuseractivity
```

### Technologies
+ Python
+ GitHub REST API
+ JSON
+ urllib
+ Command-Line Interface(CLI)

### What I Learned
+ How to make API requests using Python
+ How REST APIs work
+ How to parse JSON responses
+ How to use command-line arguments
+ How to handle API and network errors
+ How to work with nested dictionaries and lists
i i
