# Ruby Code Analysis plugin for Sublime Text 2

## Installation

Install the `flog` gem

`rvm use system && sudo gem install flog && rvm use default`


Clone the plugin in your `Packages` dir

```
cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/
git clone git@github.com:MrRuru/flog-sublime-plugin.git
```

## Use

In a ruby file

* Launch your command prompt (Cmd + Shift + P on a Mac)
* Look for "Flog Code Analysis"
* Select it

You should have a quick panel with the overall score of your file, and the most offending methods.
If you don't, file an issue.
