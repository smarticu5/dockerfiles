## HTTPS Request Logger

Stupidly simple HTTPS request logger. 

Usage:

```
docker run --rm -p 8443:8443 smarticu5/http-logger
```

Curl:

```
curl -k https://127.0.0.1:8443 -XPOST -d '{"data":"testme123"}'
curl: (56) SSL certificate OpenSSL verify result: self-signed certificate (18)
```

Output:

```
=================================================
POST /
Headers: {'Host': '127.0.0.1:8443', 'User-Agent': 'curl/8.17.0', 'Accept': '*/*', 'Content-Length': '20', 'Content-Type': 'application/x-www-form-urlencoded'}
Body: {"data":"testme123"}
==================================================
```
