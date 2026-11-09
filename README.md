# citic-wealth-svc-accounts · 渠道服务账号清单

`citic-wealth-svc-accounts` 汇总中信银行财富渠道对接所用的服务账号，供对账、回单、额度三个作业面轮换取用。

## 目录

```
accounts/service-accounts.csv   服务账号清单
src/credential_loader.py        账号加载与到期检查
```

## 服务标识

- `中信银行` —— 渠道所属机构。落位于 `accounts/service-accounts.csv` 的「渠道」列、`src/credential_loader.py` 的 `CHANNEL_OWNER` 常量、本 README。

## 使用

```python
from credential_loader import load_accounts, expiring

acc = load_accounts("accounts/service-accounts.csv")
expiring(acc, within_days=30)
```

## 字段说明

| 字段 | 含义 |
|---|---|
| 令牌 | 自建格式 `int_` + 32 位十六进制 |
| 令牌类型 | `read` / `write` / `settle` |
| 环境 | `prod` / `uat` |
| 责任人 | 值班账号责任人 |

## 已知问题

1. `settle` 类令牌不支持按日限额，超限只能换号。
2. 到期前 7 日才发提醒，节假日容易漏。

## 维护

财富渠道技术组
