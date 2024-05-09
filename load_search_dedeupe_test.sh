locust -f wms_svc_listing/locust_search_dedupe.py --web-host=localhost --host https://svc-st.moxiworks.com --users 10 \
--spawn-rate 2
