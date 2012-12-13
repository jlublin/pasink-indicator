# For now this will use pactl and pacmd until I have figured out how to use libpulseaudio

# >>> from subprocess import check_output
# >>> a = check_output(['ls', '-l'])

from gi.repository import Gtk, GLib
from gi.repository import AppIndicator3

from subprocess import check_output,call
import re

class Indicator:
	def __init__(self):
		self.indicator = AppIndicator3.Indicator.new('pulsesinker', 'onboard-mono', AppIndicator3.IndicatorCategory.HARDWARE)

		self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)

		self.UpdateSinks()

		self.indicator.set_label('PulseSinker', '')

	def UpdateSinks(self):
		self.GetSinks()

		self.menu = Gtk.Menu()
		
		for sink in self.sinks:
			item = Gtk.MenuItem()
			item.set_label(sink)
			item.connect('activate', self.OnSink)
			item.show()
			self.menu.append(item)

		item = Gtk.MenuItem()
		item.set_label('Exit')
		item.connect('activate', self.OnExit)
		item.show()
		self.menu.append(item)

		self.menu.show()
		self.indicator.set_menu(self.menu)


	def GetSinks(self):
		pactl_output = check_output(['pactl', 'list'])
		self.sinks = re.findall('Sink #.*', pactl_output)

	def SetSink(self, sink):
		call(['pacmd', 'set-default-sink', sink[6:]])

	def OnSink(self, event):
		sink = event.get_label()
		self.SetSink(sink)

	def OnExit(self, event):
		Gtk.main_quit()

	def main(self):
		Gtk.main()

if __name__ == "__main__":
	i = Indicator()
	i.main()
