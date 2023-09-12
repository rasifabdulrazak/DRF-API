from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class FileValidator:
    """
    Validator class for validate size
    and extension of uploading files.

    The @deconstructible decorator in Django
    is used to make a class deconstructible,
    which means that Django can serialize
    and deserialize instances of that class.
    It is typically used for classes that
    are defined outside of models but are
    referenced in model fields.
    """

    def __init__(
        self, max_size: float = None, allowed_extensions: list = None
    ):
        if max_size:
            self.max_size = float(max_size)
            self.max_size_in_bytes = self.max_size * (1024 * 1024)
        else:
            self.max_size = None
        self.allowed_extensions = allowed_extensions

    def __call__(self, current_file, **kwargs):
        errors = []
        if self.max_size:
            current_file_size_in_mb = round(
                current_file.size / (1024 * 1024), 2
            )
            if current_file.size > self.max_size_in_bytes:
                errors.append(
                    f"Uploaded file size must be less than {self.max_size} MB, current file size is {current_file_size_in_mb} MB"
                )

        if self.allowed_extensions:
            name = current_file.name
            if name:
                extension = name.split(".").pop(-1)
                if extension not in self.allowed_extensions:
                    errors.append("uploaded file extension not allowed")

        if errors:
            raise ValidationError(errors)
