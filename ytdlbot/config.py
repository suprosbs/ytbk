#!/usr/local/bin/python3
# coding: utf-8

# ytdlbot - config.py
# 8/28/21 15:01
#

__author__ = "Benny <benny.think@gmail.com>"

import os

# general settings
WORKERS: int = int(os.getenv("WORKERS", 100))
APP_ID: int = int(os.getenv("APP_ID", 198214))
APP_HASH = os.getenv("APP_HASH", "1234b90")
TOKEN = os.getenv("TOKEN", "1234")

REDIS = os.getenv("REDIS", "redis")

ENABLE_VIP = os.getenv("VIP", False)
OWNER = os.getenv("OWNER", "BennyThink")

# limitation settings
AUTHORIZED_USER: str = os.getenv("AUTHORIZED_USER", "")
# membership requires: the format could be username(without @ sign)/chat_id of channel or group.
# You need to add the bot to this group/channel as admin
REQUIRED_MEMBERSHIP: str = os.getenv("REQUIRED_MEMBERSHIP", "")


MYSQL_HOST = os.getenv("MYSQL_HOST", "mysql")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASS = os.getenv("MYSQL_PASS", "root")

ARCHIVE_ID = os.getenv("ARCHIVE_ID")

ENABLE_FFMPEG = os.getenv("ENABLE_FFMPEG", False)
AUDIO_FORMAT = os.getenv("AUDIO_FORMAT")

PLAYLIST_SUPPORT = os.getenv("PLAYLIST_SUPPORT", False)
M3U8_SUPPORT = os.getenv("M3U8_SUPPORT", False)
ENABLE_ARIA2 = os.getenv("ENABLE_ARIA2", False)

RCLONE_PATH = os.getenv("RCLONE")

# payment settings
PROVIDER_TOKEN = os.getenv("PROVIDER_TOKEN") or "1234"
FREE_DOWNLOAD = os.getenv("FREE_DOWNLOAD", 5)
EXPIRE = 24 * 3600
TOKEN_PRICE = os.getenv("BUY_UNIT", 20)  # one USD=20 credits

PREMIUM_USER = int(os.getenv("PREMIUM_USER", "0"))

# For advance users
# Please do not change, if you don't know what these are.
TG_PREMIUM_MAX_SIZE = 4000 * 1024 * 1024
TG_NORMAL_MAX_SIZE = 2000 * 1024 * 1024
CAPTION_URL_LENGTH_LIMIT = 150

RATE_LIMIT = os.getenv("RATE_LIMIT", 120)
# This will set the value for the tmpfile path(download path). If not, will return None and use system’s default path.
# Please ensure that the directory exists and you have necessary permissions to write to it.
TMPFILE_PATH = os.getenv("TMPFILE_PATH")


class FileTooBig(Exception):
    pass
