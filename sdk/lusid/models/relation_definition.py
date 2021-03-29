# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2803
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class RelationDefinition(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'version': 'Version',
        'relation_definition_id': 'ResourceId',
        'source_entity_domain': 'str',
        'target_entity_domain': 'str',
        'display_name': 'str',
        'outward_description': 'str',
        'inward_description': 'str',
        'life_time': 'str',
        'constraint_style': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'version': 'version',
        'relation_definition_id': 'relationDefinitionId',
        'source_entity_domain': 'sourceEntityDomain',
        'target_entity_domain': 'targetEntityDomain',
        'display_name': 'displayName',
        'outward_description': 'outwardDescription',
        'inward_description': 'inwardDescription',
        'life_time': 'lifeTime',
        'constraint_style': 'constraintStyle',
        'links': 'links'
    }

    required_map = {
        'version': 'optional',
        'relation_definition_id': 'optional',
        'source_entity_domain': 'optional',
        'target_entity_domain': 'optional',
        'display_name': 'optional',
        'outward_description': 'optional',
        'inward_description': 'optional',
        'life_time': 'optional',
        'constraint_style': 'optional',
        'links': 'optional'
    }

    def __init__(self, version=None, relation_definition_id=None, source_entity_domain=None, target_entity_domain=None, display_name=None, outward_description=None, inward_description=None, life_time=None, constraint_style=None, links=None):  # noqa: E501
        """
        RelationDefinition - a model defined in OpenAPI

        :param version: 
        :type version: lusid.Version
        :param relation_definition_id: 
        :type relation_definition_id: lusid.ResourceId
        :param source_entity_domain:  The entity domain of the source entity object.
        :type source_entity_domain: str
        :param target_entity_domain:  The entity domain of the target entity object.
        :type target_entity_domain: str
        :param display_name:  The display name of the relation.
        :type display_name: str
        :param outward_description:  The description to relate source entity object and target entity object
        :type outward_description: str
        :param inward_description:  The description to relate target entity object and source entity object
        :type inward_description: str
        :param life_time:  Describes how the relations can change over time, allowed values are \"Perpetual\" and \"TimeVariant\"
        :type life_time: str
        :param constraint_style:  Describes the uniqueness and cardinality for relations with a specific source entity object and relations under this definition. Allowed values are \"Property\" and \"Collection\", defaults to \"Collection\" if not specified.
        :type constraint_style: str
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501

        self._version = None
        self._relation_definition_id = None
        self._source_entity_domain = None
        self._target_entity_domain = None
        self._display_name = None
        self._outward_description = None
        self._inward_description = None
        self._life_time = None
        self._constraint_style = None
        self._links = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if relation_definition_id is not None:
            self.relation_definition_id = relation_definition_id
        self.source_entity_domain = source_entity_domain
        self.target_entity_domain = target_entity_domain
        self.display_name = display_name
        self.outward_description = outward_description
        self.inward_description = inward_description
        self.life_time = life_time
        self.constraint_style = constraint_style
        self.links = links

    @property
    def version(self):
        """Gets the version of this RelationDefinition.  # noqa: E501


        :return: The version of this RelationDefinition.  # noqa: E501
        :rtype: Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this RelationDefinition.


        :param version: The version of this RelationDefinition.  # noqa: E501
        :type: Version
        """

        self._version = version

    @property
    def relation_definition_id(self):
        """Gets the relation_definition_id of this RelationDefinition.  # noqa: E501


        :return: The relation_definition_id of this RelationDefinition.  # noqa: E501
        :rtype: ResourceId
        """
        return self._relation_definition_id

    @relation_definition_id.setter
    def relation_definition_id(self, relation_definition_id):
        """Sets the relation_definition_id of this RelationDefinition.


        :param relation_definition_id: The relation_definition_id of this RelationDefinition.  # noqa: E501
        :type: ResourceId
        """

        self._relation_definition_id = relation_definition_id

    @property
    def source_entity_domain(self):
        """Gets the source_entity_domain of this RelationDefinition.  # noqa: E501

        The entity domain of the source entity object.  # noqa: E501

        :return: The source_entity_domain of this RelationDefinition.  # noqa: E501
        :rtype: str
        """
        return self._source_entity_domain

    @source_entity_domain.setter
    def source_entity_domain(self, source_entity_domain):
        """Sets the source_entity_domain of this RelationDefinition.

        The entity domain of the source entity object.  # noqa: E501

        :param source_entity_domain: The source_entity_domain of this RelationDefinition.  # noqa: E501
        :type: str
        """

        self._source_entity_domain = source_entity_domain

    @property
    def target_entity_domain(self):
        """Gets the target_entity_domain of this RelationDefinition.  # noqa: E501

        The entity domain of the target entity object.  # noqa: E501

        :return: The target_entity_domain of this RelationDefinition.  # noqa: E501
        :rtype: str
        """
        return self._target_entity_domain

    @target_entity_domain.setter
    def target_entity_domain(self, target_entity_domain):
        """Sets the target_entity_domain of this RelationDefinition.

        The entity domain of the target entity object.  # noqa: E501

        :param target_entity_domain: The target_entity_domain of this RelationDefinition.  # noqa: E501
        :type: str
        """

        self._target_entity_domain = target_entity_domain

    @property
    def display_name(self):
        """Gets the display_name of this RelationDefinition.  # noqa: E501

        The display name of the relation.  # noqa: E501

        :return: The display_name of this RelationDefinition.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this RelationDefinition.

        The display name of the relation.  # noqa: E501

        :param display_name: The display_name of this RelationDefinition.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def outward_description(self):
        """Gets the outward_description of this RelationDefinition.  # noqa: E501

        The description to relate source entity object and target entity object  # noqa: E501

        :return: The outward_description of this RelationDefinition.  # noqa: E501
        :rtype: str
        """
        return self._outward_description

    @outward_description.setter
    def outward_description(self, outward_description):
        """Sets the outward_description of this RelationDefinition.

        The description to relate source entity object and target entity object  # noqa: E501

        :param outward_description: The outward_description of this RelationDefinition.  # noqa: E501
        :type: str
        """

        self._outward_description = outward_description

    @property
    def inward_description(self):
        """Gets the inward_description of this RelationDefinition.  # noqa: E501

        The description to relate target entity object and source entity object  # noqa: E501

        :return: The inward_description of this RelationDefinition.  # noqa: E501
        :rtype: str
        """
        return self._inward_description

    @inward_description.setter
    def inward_description(self, inward_description):
        """Sets the inward_description of this RelationDefinition.

        The description to relate target entity object and source entity object  # noqa: E501

        :param inward_description: The inward_description of this RelationDefinition.  # noqa: E501
        :type: str
        """

        self._inward_description = inward_description

    @property
    def life_time(self):
        """Gets the life_time of this RelationDefinition.  # noqa: E501

        Describes how the relations can change over time, allowed values are \"Perpetual\" and \"TimeVariant\"  # noqa: E501

        :return: The life_time of this RelationDefinition.  # noqa: E501
        :rtype: str
        """
        return self._life_time

    @life_time.setter
    def life_time(self, life_time):
        """Sets the life_time of this RelationDefinition.

        Describes how the relations can change over time, allowed values are \"Perpetual\" and \"TimeVariant\"  # noqa: E501

        :param life_time: The life_time of this RelationDefinition.  # noqa: E501
        :type: str
        """

        self._life_time = life_time

    @property
    def constraint_style(self):
        """Gets the constraint_style of this RelationDefinition.  # noqa: E501

        Describes the uniqueness and cardinality for relations with a specific source entity object and relations under this definition. Allowed values are \"Property\" and \"Collection\", defaults to \"Collection\" if not specified.  # noqa: E501

        :return: The constraint_style of this RelationDefinition.  # noqa: E501
        :rtype: str
        """
        return self._constraint_style

    @constraint_style.setter
    def constraint_style(self, constraint_style):
        """Sets the constraint_style of this RelationDefinition.

        Describes the uniqueness and cardinality for relations with a specific source entity object and relations under this definition. Allowed values are \"Property\" and \"Collection\", defaults to \"Collection\" if not specified.  # noqa: E501

        :param constraint_style: The constraint_style of this RelationDefinition.  # noqa: E501
        :type: str
        """

        self._constraint_style = constraint_style

    @property
    def links(self):
        """Gets the links of this RelationDefinition.  # noqa: E501


        :return: The links of this RelationDefinition.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this RelationDefinition.


        :param links: The links of this RelationDefinition.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RelationDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other