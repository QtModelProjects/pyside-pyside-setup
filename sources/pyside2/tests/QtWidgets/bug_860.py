#############################################################################
##
## Copyright (C) 2016 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of the test suite of Qt for Python.
##
## $QT_BEGIN_LICENSE:GPL-EXCEPT$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3 as published by the Free Software
## Foundation with exceptions as appearing in the file LICENSE.GPL3-EXCEPT
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "util"))

from PySide2.QtCore import QSignalMapper
from PySide2.QtWidgets import QCheckBox

from helper.usesqapplication import UsesQApplication

class MultipleSlotTest(UsesQApplication):
    def cb_changed(self, i):
        self._changed = True

    def cb_changedVoid(self):
        self._changed = True

    def testSignalMapper(self):
        checkboxMapper = QSignalMapper()
        box = QCheckBox('check me')
        box.stateChanged.connect(checkboxMapper.map)

        checkboxMapper.setMapping(box, box.text())
        checkboxMapper.mapped[str].connect(self.cb_changed)
        self._changed = False
        box.setChecked(True)
        self.assertTrue(self._changed)

    def testSimpleSignal(self):
        box = QCheckBox('check me')
        box.stateChanged[int].connect(self.cb_changedVoid)
        self._changed = False
        box.setChecked(True)
        self.assertTrue(self._changed)

if __name__ == '__main__':
    unittest.main()
