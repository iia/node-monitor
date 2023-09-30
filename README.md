# Node Monitor

Monitor network nodes.

## Setup

Add the following to user crontab (```crontab -e```):

```
@reboot cd <GIT_REPO_ROOT> && python3 view.py
* * * * * cd <GIT_REPO_ROOT> && python3 report.py
```
