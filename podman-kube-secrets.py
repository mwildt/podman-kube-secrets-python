import argparse
import base64
import yaml

def create_kubernetes_secret(secret_name, string_data):
    encoded_data = base64.b64encode(string_data.encode()).decode()

    secret = {
        'apiVersion': 'v1',
        'kind': 'Secret',
        'metadata': {
            'name': secret_name
        },
        'data': {
            secret_name: encoded_data
        }
    }

    # Convert the dictionary to a YAML string
    yaml_secret = yaml.dump(secret, default_flow_style=False)
    return yaml_secret

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="a simple utility program for the correct generation of podman secrets when using podman play kube")

    # Hinzufügen von Argumenten/Flags
    parser.add_argument('--name', '-n',
                        type=str,
                        required=True,
                        help='the name of the secret in the medadata of the created kubernetes secret. This is also used as the name for the data element itself.')

    parser.add_argument('--data', '-d', type=str, help='the secret value', required=True)

    parser.add_argument('--base64','-b64',
                        action='store_true',
                        help='if specified, the generated result will be encoded in base64')

    # Argumente parsen
    args = parser.parse_args()

    yaml_secret = create_kubernetes_secret(args.name, args.data)

    if args.b64 :
        print(base64.b64encode(yaml_secret.encode()).decode())
    else:
        print(yaml_secret)
