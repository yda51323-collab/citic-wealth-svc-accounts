# -*- coding: utf-8 -*-
"""渠道服务账号加载与到期检查。"""
import csv
import datetime

CHANNEL_OWNER = "中信银行"
TOKEN_PREFIX = "int_"


def load_accounts(path):
    rows = []
    with open(path, newline="", encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            if not r["令牌"].startswith(TOKEN_PREFIX):
                raise ValueError("unexpected token format: %s" % r["账号"])
            r["过期日"] = datetime.date.fromisoformat(r["过期日"])
            rows.append(r)
    return rows


def expiring(rows, within_days=30):
    edge = datetime.date.today() + datetime.timedelta(days=within_days)
    return [r for r in rows if r["过期日"] <= edge and r["环境"] == "prod"]


def by_channel(rows, channel=CHANNEL_OWNER):
    return [r for r in rows if r["渠道"].startswith(channel)]
