import unittest

from point_of_sale import (EMPTY_BARCODE_ERROR, LIST_WITH_INVALID_ERROR,
                           NOT_FOUND_BARCODE_ERROR, PRICES, pos, total)


class TestPointOfSale(unittest.TestCase):

    def setUp(self):
        self.empty_barcode = ''
        self.nines_barcode = '99999'
        self.not_found_barcode = '12890'
        self.valid_barcode = '12345'

    def test_empty_barcode_should_return_error_message(self):
        self.assertEqual(pos(self.empty_barcode), EMPTY_BARCODE_ERROR)

    def test_99999_barcode_should_return_error_message(self):
        self.assertEqual(pos(self.nines_barcode), NOT_FOUND_BARCODE_ERROR)

    def test_invalid_barcode_should_return_error_message(self):
        self.assertEqual(pos(self.not_found_barcode), NOT_FOUND_BARCODE_ERROR)

    def test_valid_barcode_should_return_price(self):
        self.assertEqual(
            pos(self.valid_barcode), PRICES.get(self.valid_barcode))

    def test_barcodes_list_with_invalid_should_return_error(self):
        mixed_barcodes = [self.valid_barcode, self.nines_barcode]
        self.assertEqual(
            total(mixed_barcodes), LIST_WITH_INVALID_ERROR)

    def test_valid_barcodes_list_should_return_total(self):
        valid_barcodes = [self.valid_barcode, self.valid_barcode]
        self.assertEqual(
            total(valid_barcodes), PRICES.get(self.valid_barcode)*2)


if __name__ == '__main__':
    unittest.main()
