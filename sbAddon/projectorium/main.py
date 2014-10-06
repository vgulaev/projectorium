import sublime, sublime_plugin

class makesnipCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, Worlddfdff!")
