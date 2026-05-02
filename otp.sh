#!/bin/bash
# USCIS Case Watcher - OTP Generation Script
# Add to your shell config: alias uscis-otp='/path/to/otp.sh'

cd "$(dirname "$0")"
uv run generate_otp.py "$@"
