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


class Schema(Model):
    """Schema.

    :param entity:
    :type entity: str
    :param href:
    :type href: str
    :param values:
    :type values: dict[str, ~lusid.models.FieldSchema]
    :param links:
    :type links: list[~lusid.models.Link]
    """

    _attribute_map = {
        'entity': {'key': 'entity', 'type': 'str'},
        'href': {'key': 'href', 'type': 'str'},
        'values': {'key': 'values', 'type': '{FieldSchema}'},
        'links': {'key': 'links', 'type': '[Link]'},
    }

    def __init__(self, entity=None, href=None, values=None, links=None):
        super(Schema, self).__init__()
        self.entity = entity
        self.href = href
        self.values = values
        self.links = links
