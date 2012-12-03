
from gi.repository import Gtk, GLib
from gi.repository import AppIndicator3

class Indicator:
	def __init__(self):
		self.indicator = AppIndicator3.Indicator.new('pulsesinker', 'onboard-mono', AppIndicator3.IndicatorCategory.HARDWARE)

		self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)

		self.menu = Gtk.Menu()

		item = Gtk.MenuItem()
		item.set_label('Exit')
		item.connect('activate', self.exit)
		item.show()
		self.menu.append(item)

		self.menu.show()
		self.indicator.set_menu(self.menu)

		self.indicator.set_label('PulseSinker', '')

	def exit(self, event):
		Gtk.main_quit()

	def main(self):
		Gtk.main()

if __name__ == "__main__":
	i = Indicator()
	i.main()
