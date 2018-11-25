# coding=utf-8
# --------------------------------------------------------------------------
# Copyright © 2018 FINBOURNE TECHNOLOGY LTD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CreateInstrumentPropertyRequest(Model):
    """CreateInstrumentPropertyRequest.

    :param instrument_property_key: The property key of the property, e.g,
     'Instrument/default/Isin'
    :type instrument_property_key: str
    :param property: The value of the property, which must not be empty or
     null. e.g, 'US0378331005'
    :type property: ~lusid.models.PropertyValue
    """

    _attribute_map = {
        'instrument_property_key': {'key': 'instrumentPropertyKey', 'type': 'str'},
        'property': {'key': 'property', 'type': 'PropertyValue'},
    }

    def __init__(self, instrument_property_key=None, property=None):
        super(CreateInstrumentPropertyRequest, self).__init__()
        self.instrument_property_key = instrument_property_key
        self.property = property
