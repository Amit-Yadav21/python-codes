from bs4 import BeautifulSoup
import requests,json,os


url = 'https://www.imdb.com/title/tt0066763/'
url_details = requests.get(url)
# print(url_details.text)

soup = BeautifulSoup(url_details.text,'html.parser')

def scrape_movie_details():

    main_div = soup.find('div',class_="TitleBlock__Container-sc-1nlhx7j-0 hglRHk")
    # print(main_div)

    main_div2 = soup.find('div',class_="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt")
    # print(main_div2)

    h1 = main_div2.find('h1', class_="TitleHeader__TitleText-sc-1wu6n3d-0 dxSWFG")
    # print(h1)

    movies_name = []
    movies_director = []
    movies_country = []
    movies_language = []
    movies_poster_image_url = []
    # movies_bio = ''

    #................................................ MOVIES NAME ?
    title = h1.get_text()
    movies_name.append(title)
    # print(title)

    #................................................. DIRECTOR NAME ?
    div_director = soup.find('div',class_="ipc-metadata-list-item__content-container")
    # print(div_director)
    ul = div_director.find('li',class_="ipc-inline-list__item").a.get_text()
    # print(ul)
    movies_director.append(ul)
    # print(movies_director)

    #................................................. country name ?
    seciton = soup.find("section", attrs={"class":"ipc-page-section ipc-page-section--base celwidget", "cel_widget_id":"StaticFeature_Details"})

    li1 = seciton.find("li", attrs={"data-testid":"title-details-origin"})
    li2 = seciton.find("li", attrs={"data-testid":"title-details-languages"})
    # print(li1, li2)

    countries = li1.find_all("li", class_="ipc-inline-list__item")
    country_list = []
    for i in countries:
        country_list.append(i.a.get_text())
    # print(country_list)

    # movies_country.append(country_list)
    # print(movies_country)


    #................................................. Language name ?
    languages =  li2.find_all("li", class_="ipc-inline-list__item")
    language_list = []
    for i in languages:
        language_list.append(i.a.get_text())
    
    # print(language_list)

    #................................................. poster_image_url ?
    div_poster_image_url = soup.find('div',class_="ipc-poster ipc-poster--baseAlt ipc-poster--dynamic-width Poster__CelPoster-sc-6zpm25-0 kPdBKI celwidget ipc-sub-grid-item ipc-sub-grid-item--span-2")
    # print(div_poster_image_url)

    ul = div_poster_image_url.find('a',class_="ipc-lockup-overlay ipc-focusable" )['href']
    # print(ul)
    movies_poster_image_url.append(ul)
    # print(movies_poster_image_url)

    #................................................. Bio ?
    div_bio = soup.find('div',class_="GenresAndPlot__ContentParent-sc-cum89p-8 hTqGWn Hero__GenresAndPlotContainer-sc-kvkd64-11 iEHpKn")

    span = div_bio.find('span',class_="GenresAndPlot__TextContainerBreakpointXS_TO_M-sc-cum89p-0 kHlJyu").get_text()
    # print(span)

    
    


scrape_movie_details()