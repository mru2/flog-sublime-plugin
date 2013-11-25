import sublime, sublime_plugin
import subprocess
import string
import re

# Install
# (rvm use system)
# sudo gem install flog

class FlogCommand(sublime_plugin.WindowCommand):

  def letter_score(self, score):
    if score < 50:
      return "A"
    elif score < 100:
      return "B"
    elif score < 150:
      return "C"
    elif score < 200:
      return "D"
    elif score < 300:
      return "E"
    else:
      return "F"

  @staticmethod
  def process_line(line):
    matches = re.findall(r"([\d|\.]+): ([\w|#|:]+).*?(\d+)", line)
    if matches:
      score = matches[0][0]
      method = matches[0][1]
      line = matches[0][2]
      return score + " - " + method + " [" + line + "]"

    else:
      return None

  def run(self):

    file_name = self.window.active_view().file_name()

    # Get the results of the analysis
    output =  subprocess.Popen( ("flog " + file_name), stdout=subprocess.PIPE, shell=True).stdout.read()
    lines = string.split(output, '\n')

    # Extract the headers
    total_line = lines.pop(0)
    method_average_line = lines.pop(0)
    lines.pop(0) # Blank line


    # Get the total score, and method average
    total_score = re.search(r"(\d|\.)+", total_line).group()
    total_note = self.letter_score(float(total_score))

    panel_output = []
    panel_output.append ( "Score : " + total_note + " ( " + total_score + " )" )
    panel_output.append ("")
    panel_output.append ("High scoring methods :")

    # Get the method details
    panel_output.extend( filter(None, map(self.process_line, lines)) )

    # Now get the data for each line with a problem
    self.window.show_quick_panel(panel_output, None)

