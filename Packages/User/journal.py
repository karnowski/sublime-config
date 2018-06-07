import sublime, sublime_plugin, os
from datetime import datetime

class JournalCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    home = os.environ["HOME"]
    today = datetime.today()
    placeholder_text = today.strftime("# Journal : %Y-%m-%d %H:%M")
    journal_dir = home + "/Dropbox/Documents/Adzerk/journal"
    month_dir = journal_dir + today.strftime("/%Y-%m %B")
    new_file = month_dir + today.strftime("/%Y-%m-%d-%H:%M.md")

    if not os.path.exists(month_dir):
      os.makedirs(month_dir)

    f = open(new_file,'w')
    f.write(placeholder_text + '\n\n')
    f.close()

    self.view.window().open_file(new_file)
