# Given the client ID and tenant ID for an app registered in Azure,
# provide an Azure AD access token and a refresh token.

# If the caller is not already signed in to Azure, the caller's
# web browser will prompt the caller to sign in first.

# pip install msal
from msal import PublicClientApplication
import sys

# You can hard-code the registered app's client ID and tenant ID here,
# or you can provide them as command-line arguments to this script.
client_id = '4063f5d7-c549-4453-a3a5-f039d0eac003'
tenant_id = 'f914162d-c0c3-490b-93d5-1d8cfe1a4799/B2C_1_SignUpIn'

# Do not modify this variable. It represents the programmatic ID for
# Azure Databricks along with the default scope of '/.default'.
scopes = ['email', 'https://accounts.fusyona.com/api/WriteUserProfileAPI', "https://accounts.fusyona.com/api/ReadUserProfileAPI"]

# Check for too few or too many command-line arguments.
#if (len(sys.argv) > 1) and (len(sys.argv) != 3):
#  print("Usage: get-tokens.py <client ID> <tenant ID>")
#  exit(1)

# If the registered app's client ID and tenant ID are provided as
# command-line variables, set them here.
if len(sys.argv) > 1:
  client_id = sys.argv[1]
  tenant_id = sys.argv[2]

app = PublicClientApplication(
  client_id = client_id,
  authority = "https://accounts.fusyona.com/" + tenant_id
)

acquire_tokens_result = app.acquire_token_interactive(
  scopes = scopes,
)

if 'error' in acquire_tokens_result:
  print("Error: " + acquire_tokens_result['error'])
  print("Description: " + acquire_tokens_result['error_description'])
else:
  print("Access token:\n")
  print(acquire_tokens_result['id_token'])
  print("\nRefresh token:\n")
  print(acquire_tokens_result['refresh_token'])