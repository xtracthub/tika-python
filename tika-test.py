
import tika
from tika import parser

tika.TikaClientOnly = True

# print(tika.TIKA_PATH)
# tika.tika.TikaServerJar = "file://tika-tester/tika-server-1.24-bin/tika-server.jar"

# print(tika.tika.TikaServerClasspath)

parsed = parser.from_file('setup.py')
print(parsed)

# print(tika.tika.TikaServerJar)
