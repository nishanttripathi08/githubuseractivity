import sys, urllib.request, json

if len(sys.argv) == 2:
    username = sys.argv[1]
    url = f"https://api.github.com/users/{username}/events"
    headers = {"User-Agent" : "GitHub User Activity API"}

    request = urllib.request.Request(url, headers=headers) # Creates Request object
    try:
        with urllib.request.urlopen(request) as response: # Saves information in response variable; automatically closes when finished
            raw_data = response.read() # Reads data in bytes
            info = json.loads(raw_data.decode("utf-8")) # Decodes bytes into a Python string with JSON and then converts the JSON into normal Python objects
            for index in range(len(info)):
                event = info[index]
                eventType = event["type"]
                repoName = event["repo"]["name"]
                match eventType:
                    case "PushEvent":
                        print(f"Pushed commits to {repoName}")
                    case "IssuesEvent":
                        match event["payload"]["action"]:
                            case "opened":
                                print(f"Opened a new issue in {repoName}")
                            case "closed":
                                print(f"Closed a new issue in {repoName}")
                            case "reopened":
                                print(f"Reopened a new issue in {repoName}")
                            case "assigned":
                                print(f"Assigned a new issue in {repoName}")
                            case "unassigned":
                                print(f"Unassigned a new issue in {repoName}")
                            case "labeled":
                                print(f"Labeled a new issue in {repoName}")
                            case "unlabeled":
                                print(f"Unlabeled a new issue in {repoName}")
                            case _:
                                print(f"Error: Event type({event["payload"]["action"]}) not supported under IssuesEvent")
                    case "IssueCommentEvent":
                        match event["payload"]["action"]:
                            case "created":
                                print(f"Created comment on {repoName}")
                            case "edited":
                                print(f"Edited comment on {repoName}")
                            case "deleted":
                                print(f"Deleted comment on {repoName}")
                            case _:
                                print(f"Error: Event type({event["payload"]["action"]}) not supported under IssueCommentEvent")
                    case "PullRequestEvent":
                        match event["payload"]["action"]:
                            case "opened":
                                print(f"Opened a pull request in {repoName}")
                            case "closed":
                                print(f"Closed a pull request in {repoName}")
                            case "merged":
                                print(f"Merged a pull request in {repoName}")
                            case "reopened":
                                print(f"Reopened a pull request in {repoName}")
                            case "assigned":
                                print(f"Assigned a pull request in {repoName}")
                            case "unassigned":
                                print(f"Unassigned a pull request in {repoName}")
                            case "labeled":
                                print(f"Labeled a pull request in {repoName}")
                            case "unlabeled":
                                print(f"Unlabeled a pull request in {repoName}")
                            case _:
                                print(f"Error: Event type({event["payload"]["action"]}) not supported under PullRequestEvent")
                    case "CreateEvent":
                        refType = event["payload"]["ref_type"]
                        print(f"Created a {refType} in {repoName}")
                    case "DeleteEvent":
                        refType = event["payload"]["ref_type"]
                        print(f"Deleted a {refType} in {repoName}")
                    case _:
                        print(f"Error: Event type({eventType}) not supported")
    except urllib.error.HTTPError as e:
        print("Error: Invalid username")
    except urllib.error.URLError as e:
        print("Error: Server failed")
else:
    print("Error: Command must be in format \"python3 main.py <username>\"")