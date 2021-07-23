locust -f branding/locust_branding.py --web-host=localhost --host https://svc-qa.moxiworks.com --users 2000 \
--spawn-rate 2000 --csv branding/reports/branding
