# Remembrance about window
# Copyright (C) 2023 Sasha Hale <dgsasha04@gmail.com>
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of  MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

from remembrance import info
from gi.repository import Adw, Gtk
from gettext import gettext as _

def about_window():
    return Adw.AboutWindow(
        modal = True,
        application_name = info.app_name,
        application_icon = info.app_id,
        license_type = Gtk.License.GPL_3_0,
        version = info.version,
        developer_name = 'Sasha Hale',
        copyright = _('Copyright 2023 Sasha Hale'),
        website = 'https://github.com/dgsasha/remembrance',
        developers = ['Sasha Hale https://github.com/dgsasha'],
        issue_url = 'https://github.com/dgsasha/remembrance/issues',
    )