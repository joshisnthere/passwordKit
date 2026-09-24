# Password Toolkit

Type a password to see its entropy and a rough crack-time estimate, or
generate a properly random one with your own length and charset rules.
Everything runs locally -- nothing you type is sent anywhere.

## Setup

    pip install -r requirements.txt
    python main.py

Generation uses Python's `secrets` module, not `random`, so it's suitable
for actual passwords rather than just a demo.
