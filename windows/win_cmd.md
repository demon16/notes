设置windows出站规则
```bash
netsh advfirewall firewall add rule name="forbid except 114.114.114.114" dir=out action=block remoteip="0.0.0.0-114.114.114.113, 114.114.114.115-255.255.255.255"
```
---
设置电源永不休眠
```bash
powercfg -change -standby-timeout-ac 0
```
电池永不休眠
```bash
powercfg -change -standby-timeout-dc 0
```
---