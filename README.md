# RunRun

This plugin will run other plugins and commands in FlowLauncher.

# How to settup
For the first run, the script will create a settings file with one example configuration => This configuration, will open the folder with the `Settings.json` file.
You have to click this twice in FlowLauncher.

After that the `Settings.json` file has the following structure:
```JSON
{
  "Title": "Flow Launcher query"
}
```

## Here one examples for the file
```JSON
{
    "Open Configuration": "rr Open Configuration",
    "Start JupiterLab": "> C:\\PycharmProjects\\JupyterLabs\\run_jupyter_lab.ps1"
}
```
1. The first `Open Configuration` will change the query to `rr Open Configuration`. And after clicking a second time on this query, it will open the `Settings.json` folder.
2. The second `Start JupiterLab` command, will change the query to the `> C:\\PycharmProjects\\JupyterLabs\\run_jupyter_lab.ps1`. And than you can run it.

# Why I need this?
- You can create standard FlowLauncher `query`'s, which will used often, without typing it everytime. 
- You can create a list of your **favorite** `query`'s.
- You can see all your favorite `query`'s at once.
