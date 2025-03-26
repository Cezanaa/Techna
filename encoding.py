import base64


def encode_image(binary_data):

    return base64.b64encode(binary_data).decode("utf-8")