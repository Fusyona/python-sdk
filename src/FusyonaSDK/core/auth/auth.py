from msal import PublicClientApplication

app = PublicClientApplication(
    "eb936707-593e-49d3-8028-10760d5b9b29",
    authority="https://accounts.fusyona.com/f914162d-c0c3-490b-93d5-1d8cfe1a4799/B2C_1_SignUpIn")

result = None  # It is just an initial value. This variable will store the bearer token

# We now check the cache to see
# whether we already have some accounts that the end user already used to sign in before.
accounts = app.get_accounts()
if accounts:
    # If so, you could then somehow display these accounts and let end user choose
    print("Pick the account you want to use to proceed:")
    for a in accounts:
        print(a["username"])
    # Assuming the end user chose this one
    chosen = accounts[0]
    # Now let's try to find a token in cache for this account
    result = app.acquire_token_silent(["openid"], account=chosen)

if not result:
    # So no suitable token exists in cache. Let's get a new one from Azure AD.
    result = app.acquire_token_silent(scopes=["openid", "profile", "email", "https://accounts.fusyona.com/api/WriteUserProfileAPI", "https://accounts.fusyona.com/api/ReadUserProfileAPI"], account=chosen)
if "access_token" in result:
    print(result["access_token"])  # Yay!
else:
    print(result.get("error"))
    print(result.get("error_description"))
    print(result.get("correlation_id"))  # You may need this when reporting a bug