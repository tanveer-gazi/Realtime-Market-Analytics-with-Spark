import time
import random

def buildURL():
    # Génère une URL aléatoire
    url_list=['www.quicloud.com', 'www.cloudera.com', 'www.infiniteskills.com', 'flume.apache.org','hadoop.apache.org','console.amazon.com','www.globalknowledge.com','www.gigaom.com']
    return random.choice(url_list)

def buildPath():
    # Génère un chemin aléatoire
    path_list=['/index.html', '/contact.html', '/contact/submit.html', '/about.html','/products.html','/services.html','/support.html']
    return random.choice(path_list)

def buildHTTP():
    # Génère un code HTTP aléatoire
    return random.randint(200, 599)

def getHTTP():
    # Génère un statut HTTP aléatoire
    HTTP_status = [100, 101, 102, 200, 201, 202, 203, 204, 205, 206, 207, 226, 300, 301, 302, 303, 304, 305, 307, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 422, 423, 424, 426, 500, 501, 502, 503, 504, 505, 507, 510]
    return random.choice(HTTP_status)

def buildIP():
    # Génère une adresse IP aléatoire
    b1 = random.randint(0, 255)
    b2 = random.randint(0, 255)
    b3 = random.randint(0, 255)
    b4 = random.randint(0, 255)
    return f"{b1}.{b2}.{b3}.{b4}"

log_File = open('tmp/log-generator.log', 'w')

count = 0
# Daemon infini
while True:
    if count > 1000:
        count = 0
        time.sleep(5)  # Pause de 5 secondes entre les écritures
    else:
        Http = getHTTP()
        count += 1
        Http = str(Http)
        Url = buildURL()
        Path = buildPath()
        Ip = buildIP()

        line = f"HTTP:{Http} {Url} {Path} {Ip}\n"
        log_File.write(line)

log_File.close()
