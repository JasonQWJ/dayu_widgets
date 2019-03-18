#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MDivider import MDivider
from dayu_widgets.MLineEdit import MLineEdit
from dayu_widgets.MPushButton import MPushButton
from dayu_widgets.MToolButton import MToolButton
from dayu_widgets.MLabel import MLabel
from dayu_widgets.qt import *


class MLineEditTest(QWidget):
    def __init__(self, parent=None):
        super(MLineEditTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        line_edit_large = MLineEdit(size=MView.LargeSize)
        line_edit_large.setPlaceholderText('Large Size')
        line_edit_default = MLineEdit()
        line_edit_default.setPlaceholderText('Default Size')
        line_edit_small = MLineEdit(size=MView.SmallSize)
        line_edit_small.setPlaceholderText('Small Size')

        line_edit_icon = MLineEdit(text='Xiao Hua', size=MView.SmallSize)
        tool_button = MToolButton(icon=MIcon('female.svg'), size=MView.SmallSize)
        line_edit_icon.add_suffix_widget(tool_button)

        line_edit_button = MLineEdit(text='Beijing', size=MView.SmallSize)
        push_button = MPushButton(text='Go', size=MView.SmallSize, type=MPushButton.PrimaryType)
        line_edit_button.add_suffix_widget(push_button)

        line_edit_error = MLineEdit.error(size=MView.SmallSize)
        line_edit_error.setText('waring: file d:/ddd/ccc.jpg not exists.')

        line_edit_search = MLineEdit.search(size=MView.SmallSize)
        line_edit_search_engine = MLineEdit.search_engine()
        line_edit_search_engine.add_prefix_widget(
            MToolButton(icon=MIcon('filter_line.svg', '#cccccc'), size=MView.LargeSize))

        line_edit_file = MLineEdit.file()
        line_edit_folder = MLineEdit.folder()

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('different size'))
        main_lay.addWidget(line_edit_large)
        main_lay.addWidget(line_edit_default)
        main_lay.addWidget(line_edit_small)
        main_lay.addWidget(MDivider('icon/button'))
        main_lay.addWidget(line_edit_icon)
        main_lay.addWidget(line_edit_button)
        main_lay.addWidget(MDivider('preset'))

        main_lay.addWidget(MLabel('MLineEdit.error()'))
        main_lay.addWidget(line_edit_error)
        main_lay.addWidget(MLabel('MLineEdit.search()'))
        main_lay.addWidget(line_edit_search)
        main_lay.addWidget(MLabel('MLineEdit.search_engine()'))
        main_lay.addWidget(line_edit_search_engine)
        main_lay.addWidget(MLabel('MLineEdit.file()'))
        main_lay.addWidget(line_edit_file)
        main_lay.addWidget(MLabel('MLineEdit.folder()'))
        main_lay.addWidget(line_edit_folder)
        main_lay.addStretch()
        self.setLayout(main_lay)

    @Slot()
    def slot_prefix_button_clicked(self):
        print 'prefix button clicked'


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MLineEditTest()
    test.show()
    sys.exit(app.exec_())
