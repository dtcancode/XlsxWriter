###############################################################################
#
# Tests for XlsxWriter.
#
# Copyright (c), 2013-2017, John McNamara, jmcnamara@cpan.org
#

from ..excel_comparsion_test import ExcelComparisonTest
from ...workbook import Workbook


class TestCompareXLSXFiles(ExcelComparisonTest):
    """
    Test file created by XlsxWriter against a file created by Excel.

    """

    def setUp(self):
        self.maxDiff = None

        filename = 'protect01.xlsx'

        test_dir = 'xlsxwriter/test/comparison/'
        self.got_filename = test_dir + '_test_' + filename
        self.exp_filename = test_dir + 'xlsx_files/' + filename

        self.ignore_files = []
        self.ignore_elements = {}

    def test_create_file(self):
        """Test the a simple XlsxWriter file with worksheet protection."""

        workbook = Workbook(self.got_filename)

        worksheet = workbook.add_worksheet()

        unlocked = workbook.add_format({'locked': 0, 'hidden': 0})
        hidden = workbook.add_format({'locked': 0, 'hidden': 1})

        worksheet.write('A1', 1)
        worksheet.write('A2', 2, unlocked)
        worksheet.write('A3', 3, hidden)

        workbook.close()

        self.assertExcelEqual()
