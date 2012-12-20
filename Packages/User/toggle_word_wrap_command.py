import sublime, sublime_plugin

class ToggleWordWrapCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.settings().set('word_wrap', not self.view.settings().get('word_wrap'))
