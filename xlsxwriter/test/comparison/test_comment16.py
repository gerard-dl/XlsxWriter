###############################################################################
#
# Tests for XlsxWriter.
#
# Copyright (c), 2013-2020, John McNamara, jmcnamara@cpan.org
#

from ..excel_comparsion_test import ExcelComparisonTest
from ...workbook import Workbook


class TestCompareXLSXFiles(ExcelComparisonTest):
    """
    Test file created by XlsxWriter against a file created by Excel.

    """

    def setUp(self):

        self.set_filename('comment16.xlsx')

    def test_create_file(self):
        """Test the creation of a simple XlsxWriter file with comments."""

        workbook = Workbook(self.got_filename)

        worksheet = workbook.add_worksheet()

        worksheet.write('A1', 'Foo')
        worksheet.write('C7', 'Bar')
        worksheet.write('G14', 'Baz')

        worksheet.write_comment('A1', 'Some text')
        worksheet.write_comment('D1', 'Some text')
        worksheet.write_comment('C7', 'Some text')
        worksheet.write_comment('E10', 'Some text')
        worksheet.write_comment('G14', 'Some text')

        worksheet.set_comments_author('John')

        workbook.close()

        self.assertExcelEqual()
