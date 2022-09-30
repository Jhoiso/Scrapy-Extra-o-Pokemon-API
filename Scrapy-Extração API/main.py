# https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/
# https://www.digitalocean.com/community/tutorials/como-fazer-crawling-em-uma-pagina-web-com-scrapy-e-python-3-pt
# Arquvo que irá gerar um .json dos atributos pegos no site

import scrapy




class PokemonScrapper(scrapy.Spider):
    name = 'pokemon_scrapper'

    start_urls = ["https://www.serebii.net/pokedex/001.shtml"]

    def parse(self, response):
        #NOME
        dextable = response.css('.dextable')
        tr = dextable[1].css('tr')[1]
        tdNome = tr.css('td')[0]
        nome = tdNome.css('::text')

        #ID
        dextable = response.css('.dextable')
        tr = dextable[1].css('tr')[1]
        tdId = tr.css('td')[10]
        id = tdId.css('::text')

        #PESO
        dextable = response.css('.dextable')
        tr = dextable[1].css('tr')[7]
        tdPeso = tr.css('td')[2]
        peso = tdPeso.css('::text')

        #ALTURA
        dextable = response.css('.dextable')
        tr = dextable[1].css('tr')[7]
        tdAltura = tr.css('td')[1]
        altura = tdAltura.css('::text')

        #TIPO
        linkTipo = response.xpath('//td[@class="cen"]/a/@href').get()
        a = len(linkTipo) - 6
        tipo = linkTipo[9:a]
        print(tipo)

        #DANO
        tipos = [
            "Normal", "Fogo", "Agua", "Eletricidade", "Grama", "Gelo",
            "Lutador", "Poison", "Ground", "Voador", "Psic", "Inseto", "Rocha",
            "Fantasma", "Dragao"
        ]
        dano = []
        taked_damege = {}

        for i in range(0, 15):
            dextable = response.css('.dextable')
            tr = dextable[3].css('tr')[2]
            tdDano = tr.css('td')[i]
            a = tdDano.css('::text')
            a = a.get()
            a = a.replace("*", "")
            a = a.replace('""', "")
            dano.append(a)

        for k in range(0, 15):
            taked_damege[tipos[k]] = dano[k]

        #EVOLUÇAO
        linkEvolucao = response.xpath('//td[@class="pkmn"]/a/@href').getall()
        if (not linkEvolucao):
            print("SEM EVOLUCAO")

        elif (len(linkEvolucao) == 10):
            vetorLink = linkEvolucao[7:]
            vetorLink += "-"
            ev = []
            for j in range(0, 3):
                linkPoke = vetorLink[j]
                numId = "#" + str(linkPoke[9:12])

                if (numId == id.get()):
                    numEv = vetorLink[j + 1]
                    ev.append("#" + str(numEv[9:12]))
                    print(ev)

        elif (len(linkEvolucao) > 10):
            vetorLink = linkEvolucao[7:10]
            vetorLink += "-"
            ev = []
            for j in range(0, 3):
                linkPoke = vetorLink[j]
                numId = "#" + str(linkPoke[9:12])

                if (numId == id.get()):
                    numEv = vetorLink[j + 1]
                    ev.append("#" + str(numEv[9:12]))
                    print(ev)

        elif (len(linkEvolucao) < 10):
            vetorLink = linkEvolucao[7:]
            vetorLink += "-"
            ev = []
            for j in range(0, 2):
                linkPoke = vetorLink[j]
                numId = "#" + str(linkPoke[9:12])
                if (numId == id.get()):
                    numEv = vetorLink[j + 1]
                    ev.append("#" + str(numEv[9:12]))
                    print(ev)

        #Exceçao --> eevee (3 evoluçoes apartir de uma)
        if id.get() == "#133":
            ev = "#134 #135 #136"

        yield {
            "Nome": nome.get(),
            "ID": id.get(),
            "Peso": peso.get(),
            "Altura": altura.get(),
            "Tipo": tipo,
            "Dano": taked_damege,
            "Evolucao": ev
        }

        #Troca de pokemon atraves do botao do site
        link = response.xpath('//td[@align="center"]/a/@href').getall()[-1]
        a = response.urljoin(link)
        yield scrapy.Request(a, callback=self.parse)
