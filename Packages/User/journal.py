import sublime, sublime_plugin, os
from datetime import datetime

class JournalCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    home = os.environ["HOME"]
    today = datetime.today()
    placeholder_text = today.strftime("# Journal : %Y-%m-%d %H:%M")
    journal_dir = home + today.strftime("/Dropbox/Documents/Adzerk/journal/%Y-%m %B")
    new_file = journal_dir + today.strftime("/%Y-%m-%d-%H:%M.md")

    if not os.path.exists(journal_dir):
      os.makedirs(journal_dir)

    f = open(new_file,'w')
    f.write(placeholder_text + '\n\n')
    f.close()

    os.system("cd /Dropbox/Documents/Adzerk/journal; git add .")
    os.system("cd /Dropbox/Documents/Adzerk/journal; git commit -m \"update\"")

    self.view.window().open_file(new_file)
