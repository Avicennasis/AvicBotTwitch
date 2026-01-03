#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
twitchconfig.py - Configuration for AvicBot Twitch IRC Bot

This file contains sensitive configuration like OAuth tokens.
Keep this file secure and never commit real tokens to public repositories!

To get a Twitch OAuth token:
    1. Go to https://twitchapps.com/tmi/
    2. Log in with your Twitch account
    3. Copy the OAuth token (starts with "oauth:")
    4. Paste it below

Author: Léon "Avic" Simmons
License: MIT License
"""

# =============================================================================
# AUTHENTICATION
# =============================================================================

# Your Twitch OAuth token for IRC authentication
# Format: "oauth:xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
# 
# SECURITY WARNING: Never share your OAuth token or commit it to public repos!
# Consider using environment variables for production deployments.
#
# Example using environment variable:
#   import os
#   PASS = os.environ.get("TWITCH_OAUTH_TOKEN", "oauth:your_fallback_token")

PASS: str = "oauth:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
