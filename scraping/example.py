from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    data = f.read()

# print(data)

soup = BeautifulSoup(data, "html.parser")

# print(soup)

divs = soup.select("div")
# you can select classes and ids like: (.classname), (#idname)

# print(len(divs), "divs found")

# for d in divs:
#     print()
#     print(d)

print("content:", divs[0].get_text())

div2 = divs[1]

pps = div2.select("p")

print("PPS:")

for p in pps:
    print(p.get_text())

print("dailys:")
dailys = soup.select(".daily")
for d in dailys:
    print(d.get_text())


print(dailys[1].attrs["data-value"])
