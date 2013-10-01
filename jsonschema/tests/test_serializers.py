from jsonschema.tests.compat import OrderedDict, unittest
from jsonschema.validators import Draft4Validator


class SerializeMixin(object):
    def test_it_serializes_default_properties(self):
        schema = {"properties": {"foo": {"default": "bar"}}}
        result, errors = self.validator_class(schema, serialize=True).serialize({})
        self.assertEquals(result, {"foo": "bar"})
        self.assertEquals(errors, [])

    def test_it_serializes_default_properties_in_items(self):
        schema = {"items": {"properties": {"foo": {"default": "bar"}}}}
        result, errors = self.validator_class(schema, serialize=True).serialize([{}])
        self.assertEquals(result, [{"foo": "bar"}])
        self.assertEquals(errors, [])

    def test_it_serializes_properties_in_order(self):
        schema = {"properties": OrderedDict([("foo", {}), ("bar", {})])}
        validator = self.validator_class(
            schema, types={"object": OrderedDict}, serialize=True,
        )
        value = OrderedDict([("bar", 1), ("foo", 2)])
        result, errors = validator.serialize(value)
        self.assertIsInstance(result, OrderedDict)
        self.assertEquals(list(result), ["foo", "bar"])
        self.assertEquals(errors, [])

    def test_it_serializes_properties_in_order_with_dict(self):
        schema = {"properties": OrderedDict([("foo", {}), ("bar", {})])}
        validator = self.validator_class(
            schema, types={"object": (OrderedDict, dict)}, serialize=True,
        )
        value = dict([("bar", 1), ("foo", 2)])
        result, errors = validator.serialize(value)
        self.assertIsInstance(result, OrderedDict)
        self.assertEquals(list(result), ["foo", "bar"])
        self.assertEquals(errors, [])


class SerializeDraft4(SerializeMixin, unittest.TestCase):
    validator_class = Draft4Validator
