from scrapping.sites.kabum import scrap_kabum

if __name__ == "__main__":
    produtos = scrap_kabum()
    for p in produtos:
        print(f"{p['name']} - {p['price']}")