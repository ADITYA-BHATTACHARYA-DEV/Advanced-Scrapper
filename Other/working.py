import requests
from requests.exceptions import ProxyError, ReadTimeout, ConnectTimeout
proxy='http://35.91.241.89'
timeout=50
scheme_proxy_map={
    'https':proxy,
}
try:
    response=requests.get('http://ipinfo.io/json',proxies=scheme_proxy_map,timeout=timeout)
except(ProxyError,ReadTimeout,ConnectTimeout) as error:
    print('Unable to connect  to proxy: ',error)
else:
    print(response.text)