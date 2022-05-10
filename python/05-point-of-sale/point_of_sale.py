PRICES = {
    '12345': 7.25,
    '23456': 12.50
}

EMPTY_BARCODE_ERROR = 'Error: empty barcode'
NOT_FOUND_BARCODE_ERROR = 'Error: barcode not found'
LIST_WITH_INVALID_ERROR = 'Error: your barcodes contain errors'


def pos(barcode):
    if barcode == '':
        return EMPTY_BARCODE_ERROR

    if barcode == '99999' or not PRICES.get(barcode):
        return NOT_FOUND_BARCODE_ERROR

    return PRICES.get(barcode)


def total(barcodes):
    # assumption: barcodes is a list

    res = [
        pos(barcode) for barcode in barcodes
    ]

    if any(isinstance(barcode, str) for barcode in res):
        return LIST_WITH_INVALID_ERROR

    return sum(res)
