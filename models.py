from marshmallow import Schema, ValidationError, fields, validate, validates_schema


VALID_CMD_COMMANDS: tuple = (
    'filter', 'unique', 'map', 'limit', 'sort', 'regex'
)


class RequestSchema(Schema):
    """
    Model RequestSchema
    """
    cmd = fields.Str(required=True, validate=validate.OneOf(VALID_CMD_COMMANDS))
    value = fields.Str(required=True)

    # ==== ДЕКОРАТОР ПРОВЕРКИ ВАЛИДАЦИИ КОМАНД ====
    # @validates_schema()
    # def check_all_cmd_valid(self, values: dict[str, str], *args, **kwargs):
    #     if values['cmd'] not in VALID_CMD_COMMANDS:
    #         raise ValidationError('"cmd" contains invalid value')


class BatchRequestSchema(Schema):
    """
    Model BatchRequestSchema
    """
    queries = fields.Nested(RequestSchema, many=True)
    file_name = fields.Str(required=True)
