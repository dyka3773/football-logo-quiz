import base64
import io


def img_to_base64(image_path: str) -> str:
    """Converts image to base64 string.

    Args:
        image_path (str): Path to image.

    Returns:
        str: Base64 encoded image.
    """
    with open(image_path, "rb") as img_file:
        return encode_image(img_file.read())


def encode_image(image: bytes) -> str:
    """Encodes image to base64 string.

    Args:
        image (Image): Image to be encoded.

    Returns:
        str: Base64 encoded image.
    """
    return base64.b64encode(image).decode()
