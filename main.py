
import json
import xml.etree.ElementTree as ET
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import date
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from portalnowResidential import url_links
from portalnow_industrial import url_links2

# Inicializar el navegador
driver = webdriver.Chrome()

# # Lee el archivo Excel y obtiene los URLs de la columna "Referencia"
# df = pd.read_excel('enlaces_vivantial.xlsx', sheet_name='Sheet1', usecols=['link'])
#
# # Convierte los URLs en una lista
# url_list = df['link'].tolist()
#
#
# # url_list = ["https://www.solvia.es/es/propiedades/comprar/piso-barcelona-2-dormitorio-110833-174829",
# #             "https://www.solvia.es/es/propiedades/comprar/piso-bell-lloc-durgell-2-dormitorio-71710-157304",
# #             "https://www.solvia.es/es/propiedades/comprar/piso-monovar-monover-3-dormitorio-93893-119688"]



data = []
counter = 0
for url in url_links2:

    driver.get(url)


    accept_cookies_button_locator = (
    By.CSS_SELECTOR, "#mat-dialog-0 > pn-result-dialog > div > div > button:nth-child(2)")
    try:
        wait = WebDriverWait(driver, 10)
        accept_cookies_button = wait.until(EC.element_to_be_clickable(accept_cookies_button_locator))
        accept_cookies_button.click()
    except (TimeoutException, NoSuchElementException):
        print("No se pudo hacer clic en el botón de aceptar cookies o el elemento no está presente")

    # # Esperar a que el elemento esté presente en la página antes de extraer el texto
    # wait = WebDriverWait(driver, 10)


    wait = WebDriverWait(driver, 4)

    # provincia
    try:
        provincia_element = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/pn-root/pn-navigation/mat-sidenav-container/mat-sidenav-content/pn-asset-detail/div/div[1]/div[1]/div[2]")))

        provincia_text = provincia_element.text
        words = provincia_text.split(",")  # divide la cadena en palabras usando la coma como separador
        first_word = words[1]  # accede a la primera palabra antes de la coma
    except TimeoutException:
        first_word = 'N/A'

    try:
        ciudad_element = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                    "/html/body/pn-root/pn-navigation/mat-sidenav-container/mat-sidenav-content/pn-asset-detail/div/div[1]/div[1]/div[2]")))
        ciudad_text = ciudad_element.text
        words = ciudad_text.split(",")  # divide la cadena en palabras usando la coma como separador
        if len(words) > 1:
            second_word = words[0].strip()
            second_word = second_word.replace("room", "")# accede a la palabra después de la coma
        else:
            second_word = 'N/A'  # si no hay palabra después de la coma
    except TimeoutException:
        second_word = 'N/A'

    # Metros cuadrados
    try:
        metros_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/pn-root/pn-navigation/mat-sidenav-container/mat-sidenav-content/pn-asset-detail/div/div[1]/div[2]/div[2]/div[1]/span")))
        metros_text = metros_element.text

    except TimeoutException:
        metros_text = 'N/A'

    # Dormitorios
    try:
        dormitorio_element = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/pn-root/pn-navigation/mat-sidenav-container/mat-sidenav-content/pn-asset-detail/div/div[1]/div[2]/div[2]/div[2]/span")))
        dormitorio_text = dormitorio_element.text

    except TimeoutException:
        dormitorio_text = 'N/A'

    # Baños
    try:
        bano_element = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/pn-root/pn-navigation/mat-sidenav-container/mat-sidenav-content/pn-asset-detail/div/div[1]/div[2]/div[2]/div[3]/span")))
        bano_text = bano_element.text
        bano_text = bano_text.replace("Baños:", "")
    except TimeoutException:
        bano_text = 'N/A'


    # Referencia
    try:
        referencia_element = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/pn-root/pn-navigation/mat-sidenav-container/mat-sidenav-content/pn-asset-detail/div/div[2]/div/div/span")))
        referencia_text = referencia_element.text
        referencia_text = referencia_text.replace("Ref:", "")
    except TimeoutException:
        referencia_text = 'N/A'


    # Título
    try:
        title_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/pn-root/pn-navigation/mat-sidenav-container/mat-sidenav-content/pn-asset-detail/div/div[1]/div[1]/h1")))
        title_text = title_element.text
    except:
        title_text = 'N/A'


    # Descripción
    try:
        descripcion_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/pn-root/pn-navigation/mat-sidenav-container/mat-sidenav-content/pn-asset-detail/div/div[1]/div[1]/div[3]")))
        descripcion_text = descripcion_element.text
    except:
        descripcion_text = 'N/A'

    # Precio
    try:
        price_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/pn-root/pn-navigation/mat-sidenav-container/mat-sidenav-content/pn-asset-detail/div/div[2]/div/div/div/div[1]")))
        price_text = price_element.text                                         
    except:
        price_text = 'N/A'

    # Imagen principal
    try:
        main_photo_element = wait.until(EC.presence_of_element_located((By.XPATH, "//picture[@class='ng-star-inserted']//img")))
        image_source = main_photo_element.get_attribute("src")
    except:
        image_source = 'N/A'

    # #ImageSources
    # try:
    #     image_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='row']/div/div/img")))
    #     image_sources = [img.get_attribute("src") for img in image_elements]
    # except:
    #     image_sources = 'N/A'

    #imprimir todos los valores por consola
    print(f'ref: {referencia_text}, title: {title_text}, description: {descripcion_text}, metros: {metros_text}, hab: {dormitorio_text}, baños: {bano_text}, price: {price_text}, provincia: {first_word}, ciudad: {second_word}, ´MainPhoto: {image_source}')

    # Almacenar los datos en la lista
    data.append({
        "Referencia": referencia_text,
        "Title": title_text,
        "Descripcion": descripcion_text,
        "Provincia": first_word,
        "Ciudad": second_word,
        "MetrosCuadrados": metros_text,
        "Dormitorios": dormitorio_text,
        "Baños": bano_text,
        "Price": price_text,
        "MainPhoto": image_source,


    })

    # Convertir la lista de datos en un DataFrame
    df = pd.DataFrame(data, columns=['Referencia', 'Title', 'Descripcion', 'MetrosCuadrados', 'Dormitorios', 'Baños', 'Price', 'MainPhoto', 'Provincia', 'Ciudad'])
    if counter % 20 == 0:
        file_counter = counter // 20
        df.to_excel(f"properties_data_{file_counter}.xlsx", index=False, engine="openpyxl")

driver.quit()



#
# import json
# import xml.etree.ElementTree as ET
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
# from selenium.webdriver.common.by import By
# import pandas as pd
# from datetime import date
# import time
# import re
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Inicializar el navegador
# driver = webdriver.Chrome()
#
# # Lee el archivo Excel y obtiene los URLs de la columna "Referencia"
# df = pd.read_excel('enlaces_vivantial.xlsx', sheet_name='Sheet1', usecols=['link'])
#
# # Convierte los URLs en una lista
# url_list = df['link'].tolist()
#
# data = []
# counter = 0
#
# try:
#     for url in url_list:
#         driver.get(url)
#         time.sleep(10)
#
#         accept_cookies_button_locator = (By.CSS_SELECTOR, "#infocookie > p:nth-child(3) > a.btn.btn-primary.btn-sm.btn-cookie.mr-3")
#         try:
#             wait = WebDriverWait(driver, 20)
#             accept_cookies_button = wait.until(EC.element_to_be_clickable(accept_cookies_button_locator))
#             accept_cookies_button.click()
#         except (TimeoutException, NoSuchElementException):
#             print("No se pudo hacer clic en el botón de aceptar cookies o el elemento no está presente")
#
#         wait = WebDriverWait(driver, 40)
#
#         # provincia
#         try:
#             provincia_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='ficha']/h1")))
#             provincia_text = provincia_element.text
#             words = provincia_text.split()  # divide la cadena en palabras
#             last_province = words[-1]  # accede a la última palabra
#         except TimeoutException:
#             last_province = 'N/A'
#
#         # Metros cuadrados
#         try:
#             metros_element = wait.until(
#                 EC.presence_of_element_located((By.XPATH, "//*[@id='ficha']/div[3]/div[2]/ul/li[2]")))
#             metros_text = metros_element.text
#             metros_text = metros_text.replace("Superficie:", "")
#         except TimeoutException:
#             metros_text = 'N/A'
#
#         # Dormitorios
#         try:
#             dormitorio_element = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='ficha']/div[3]/div[2]/ul/li[3]")))
#             dormitorio_text = dormitorio_element.text
#             dormitorio_text = dormitorio_text.replace("Nº habitaciones:", "")
#         except TimeoutException:
#             dormitorio_text = 'N/A'
#
#         # Baños
#         try:
#             bano_element = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='ficha']/div[3]/div[2]/ul/li[4]")))
#             bano_text = bano_element.text
#             bano_text = bano_text.replace("Baños:", "")
#         except TimeoutException:
#             bano_text = 'N/A'
#
#         # Referencia
#         try:
#             referencia_element = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='ficha']/p[2]/span")))
#             referencia_text = referencia_element.text
#         except TimeoutException:
#             referencia_text = 'N/A'
#
#         # Título
#         try:
#             title_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='ficha']/h1")))
#             title_text = title_element.text
#         except:
#             title_text = 'N/A'
#
#         # Descripción
#         try:
#             descripcion_element = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='ficha']/div[2]/div/div")))
#             descripcion_text = descripcion_element.text
#         except TimeoutException:
#             descripcion_text = 'N/A'
#
#         data.append([last_province, metros_text, dormitorio_text, bano_text, referencia_text, title_text, descripcion_text])
#
# except WebDriverException:
#     driver.quit()
#     driver = webdriver.Chrome()
#     # Aquí podrías intentar realizar la acción que falló nuevamente o continuar con el siguiente URL
#
# driver.quit()
#
# df = pd.DataFrame(data, columns=["Provincia", "Metros cuadrados", "Dormitorios", "Baños", "Referencia", "Título", "Descripción"])
# df.to_csv('datos_vivanti.csv', index=False, encoding='utf-8')



# import json
# import xml.etree.ElementTree as ET
# from selenium import webdriver
# from selenium.common import NoSuchElementException, TimeoutException
# from selenium.webdriver.common.by import By
# import pandas as pd
# from datetime import date
# import time
# import re
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# urls = [[35622], [58174], [26532], [49848], [40755], [50849], [26476], [26197], [51174], [50860], [60427,26022], [26756,37996,53380], [49812], [40187], [26030,27246,26896,53394,40287,51545], [26016,39677], [50515], [51474], [60654], [38283], [26502,26408,50780], [76294,49796,39006,26651,40277,49912,26316], [76384,14745,26226,25987], [26915,40721,26026,50748,59332,49852,26763], [31899,7093,49786,54763,64582], [41126,60618,26764,24878,55197,58307,26739], [40098,52623,65107,74426,31996,2528], [49727,40270,64243,39770,52559,40868], [14095,40897,16254,50675,58514], [37596], [26779,26241,49849,61636,49913,39113], [50692], [76286], [51463,26313,52960,55585,40823,54271], [26742,51108,41197], [18747,9529,26676,6260,17655], [40911], [4510,7491], [39731], [76288], [2613,41194], [65697], [18623], [26634], [61500,64646,49949,26566,2614,52624,49806], [39777], [6889,25982], [51274,55438,2844,21749,9229,49884], [26501,26745,49813,26426], [51317,76315,40824,41196,26633,49811], [26069,21734], [16222,61410], [69,26578,49883,54635,26580,50952], [40802,40716], [26131,7479], [49916,52978,64265,49862,50765,49841,49765], [50772,26575,50682], [2682,7279,22493,2506,52743,31695], [49889,26602,50695,38005,9113,26428], [31988,39743,49730,49953,53259,26550], [51358,60431,38004], [49795], [75049,18182,49959,40733], [17817,49890], [55423,55581,24249,39061,63741,49769], [26145], [18460,20557,23004,49762,21726,2569,26379], [39729], [61902,58320], [49801,75046,19290,24867,26061,26749,31991], [63339], [49834,60781,49830,55424,2571,26485,28922], [25202,38278,49761,21819,40773,41199,26911], [65672], [31757], [60562,323,56888,26132,40789,26064,26728], [51580,40769], [26574,40863], [55582], [2664,51451,25035,18452,21114,39753,49839], [10588], [40838,9140], [52957,37691,39090,50756,51705,65066], [62317,63553], [39772,39773,40772,2640,25981,37977,49919], [19003,26410], [25196,49782], [40768,57019,49760,20830,39734,14064,21820], [40803,26743], [23395,53757], [18209,75039,26568,1064,40898], [39518,8101,11485,20494,26667,55937,51233], [26194,40714], [3580,20951], [63985,26490], [65242,51377,25030,40882,55583,65129,55337], [3584,49742,52054,61540,49879,26427,40899], [39244,40930,50602,50690,24233], [26195,64565,1598,24566,26244,49869], [26029,2659], [40801], [49898,74938], [40669,49754,19112,34576,51461,612], [41203,55580,9126,26027], [50694,63548,28997,51776,9069,26298], [51752,26505], [2418,8953,26618,26683,49785,50752,17837], [2705,11655,12592,51479,61594,25979],  [23817], [55348,26001], [2781,9032,49807,51584,75056,26294], [49892,26497,25308,2854,8135], [4470,7081,26129,26531,51477,61909,29035], [49851,8807], [26403,40072,26117,55349,25998,49810], [63369,1522,24376,26134,38277], [50768,58589,40748,61519,40852,51376], [13495], [26295,26311,40926,65462,53449,26004,4467], [50420,60649,28928,24265,26169,26746,49923], [24247,61670,576,9692,26430,49824], [26128,26304,40737], [66038,26597,41193,3824,14627,21056,21152], [26524], [26124,26243,26420,26641,39735,13269,26122], [23002,25986], [61903,26778], [25994,25995,49902,63275,49922,64537], [76201,25980,26567,52856,58318], [40917,53466], [24251], [1056,26444,26669,40667,26115,39764,6857], [12810,26323,26643,40928,49766,54954], [11463,18461,21805,23393,26325], [56073,63277,40836,75044,40905,84,8094], [21199,41204,1686], [8308,53263], [64206,40903,40908,12343,26576,74802], [54613,40687,18546,52959,915,2536,6917], [13707,15644], [64644,10524,52562,26493,7295,7478,7761], [39742,18046,16272,49856,50638,52493,61803], [26245,26590,26740,28921,50762], [14051,14072], [10507], [49911,64130,76672,26478,66209,26070,6793], [26663,37926,40924,49780,49790], [26251], [55387], [40070,40693,40813,49831,57130,74940,51445], [1307,18160], [26521,40933,75047,26074,26077,49767,40675], [26068,26076,39712,52873,3046,20042,25048], [52870,63276], [49948,52671], [26110,26307], [52056,26066,26116,26496,58414,3583], [51927,26072,66210,9153], [26709,39165,40931,49918,51164,52857], [13315,23812,24660,26109], [26113,3852], [26071], [26067], [61897,39739], [53262], [50693], [40822,49800], [49878,55192,60704,26414,24256,26525,40796], [54905,76614,63336,60771,2808,13485,26296], [26250,39678,40887,49840,76654,54833,334], [2566,16256,20644,26570,26640,51234], [39759,53451], [52963,53676,54884,56230], [40800,2864,13700,40841,49738,51578,52859], [40668], [26249,39740], [38003,40938,54909,40853,3772,25988], [17120,17182,17257,17834,18449,18698,22554], [26760,40855,64066], [13698,15639,15656,19136,26434,26504], [7879], [51484,85], [12996,22370,40806,52863,76383,26489,19569], [23822,26734], [49803,9163,18457,18658,18659,41259,26003], [49880], [40856,41258], [26153,26154,26402,26767,38760,39762], [26645,26751,49726,49775,58302,39733], [26446,26582], [83,75057,64219,3920,5198,12766,26156], [6818,6963], [50750,50777,61633,18898,39760,58417,1545], [39748,26130], [53453], [51367,52974,54925,40706,26463], [26491,31992,32137,39749,40814,40872,49903], [53463,56560,63258,26612], [53450,6667,26158,26171,26211,26383], [53461,58692], [32134,37457,40804,49823,50771,52854,53460], [31755,6897], [26458,26898,26899,26902,26904,39745,40842], [51596,53462,55835], [49832,49846], [40896,40932,41228,41233,41243,41245], [38281,40808], [26136,26151,26322,26378,28949,38010], [26646,29001], [26161,26235,26247,26315,26512,26571], [40864,40890], [8947,18189,26268,26399,29216,39725,40730], [40735,40927,50685,60028,40749,26024,39775], [26237,26637], [49797,60370,58278,60501,127,355], [9097,14594,17768], [37454,158,229,3755,7089,8250], [52971,53456,55420,40815,55191,75036,40686], [41241,41242,49733,51350,51747,52736], [40873,41150], [74807,52498,3786,9145,12994,26548,40691], [40874,41223], [26137,40677,40678,41201,41202,2661,15326], [23751,63725,64763,75034], [61812], [49853,54891], [41198,3021,14057,25033,26165,26264,26377], [26483], [63560,64279], [11693,26291,32136,40718,49868,63559], [26232,26324], [25122,25307], [50543,61821,11398,10861,12110,18748], [15643,17205,23794,26062], [74806,66021,41216,41219,41220,13740], [23139,26125], [7090,10459], [26480,763,1565,2558,3853], [51346,52055,54910,23749,61616,52847,60705], [26647,37998], [7425,18696,24342,9106,10523,20696,26155], [52430], [26744,39001,40710,40805,49820,49882,51475], [61806,39757,22501,40700,26401], [76290,76656], [49842,49863,52855,56883,61811,64189,76284], [24319,25098,26108], [74878,1229,7182,8091,8171,23795], [55190,11267,57760,6992,19378,23422], [27080], [26668], [58579,950,2756,3008,21860,21875,26649], [51366,51598,52673,52861,53268,54904], [26617,26654,40799,40900,40901,40902], [40699,40794,2439,3938,3939,7178], [41207,41213,41217,40870,61414,60178], [57020,61411,63282], [26687,29053,40666,49777,49958,50483], [60476,63528,65269,49755,40274,17210,7594], [41244,41246,41247,49844], [41234,41237,41238,41239,41240], [41225,41226,41227,41229,41230,41231,41232], [41160,41165,41167], [41148,41152,41154,41156,41157,41158], [11461], [11268], [26662,40811,25970,38990,8195,162,2787], [41170,41171,41175,41177,49792,49924], [41153,41155,41162,41163,41164], [2497,12950,14622,16724,26622,41145,41146], [41142,41205], [40698,49838,64067,41186,41189,61850,63337], [21755,60426,39245], [62258,40851], [61716,61810], [50506,50674,51095,52759,53464,61462], [57758,7180,18564,25975,26230,26621,26768], [9541], [877], [40750,41184,26106,51774], [49921,56813,56997,57015,61664,17255,16205], [40889,40937], [29052,31905,39728,40812,40835], [7214,8836,15332,23434,25031,26261,26270], [40834,52858,55202,61799,41183,41185,41188], [1426], [26604,29069], [50541,57670,64575,76289], [61804,9112,26170,26255,39768,40709,49749], [17211,18497], [50701,61802], [40832,49768,49825,49908,60563,41143,50700], [26436,26437,26443,26626], [7765,11407,22555,25968,25974,26183,26184], [53266,39744,41212,74801], [51773], [53458,54947,57505,61399,62322,76285,54899], [17117,25967,26052,26058,26059,26584,26607], [41191,18664], [51549,52428,54939,76283,76291,76363], [26236,26424], [65685,2125,6763,7525,7526,10866,23785], [51460,57994], [26522,40762,40936,49804,49809,49816], [228,2724,9018,15809,16641,23818], [66154,40681], [26644,26755,26769,41261,52977,54906,58281], [53092,64589,76097,54931], [14048,26051,26175,26305,40670,52866], [75037,40844], [60668,62672,63286,64948], [56069,57504], [26619,40833,49736,50696,54636,54651,54839], [40791,11795,22372,61717,359,2421,8742], [26407,26758], [18622,64007,13119,18445,20860,23032,26231], [40784,4461], [40767,49947,51476,61412,63538,16676], [26162,26409], [26190,1592,8092,21632,26053,26056], [26233], [42777,49897,49907,51458,52544,54867,54922], [26664,39251], [54923,63561,6542,6480,8364,26326,26660], [49821,49872], [40731,40879,42780,49748], [38009], [26628,26659], [6938,9444,11517,25969,26166,26528,26563], [61805,40843,54936], [49955,50686,52442,53090,54829,54945], [40861,40862], [4519,7000,11566,26177,26234,26404,39732], [60937,76205], [54942,13731,40860,26413,26677,56301,52764], [26670,49794], [54930,12604,64008,36419,49881], [74364,62380,49750,54900,26181], [43337,51352], [26706,40729,8881,75042,55136,76067], [26657,54917], [62259,26514,7310,54920,54932,26441,26445], [40845,4457], [60617,26431,52868,4460,26054,26173,52226], [63280,40751], [40880,55586], [11419,15176,21802,27074,26513,11456], [26620,50421,51753,53504,54912,2390,10442], [26447], [64003,64005,64006,40847,26292,51548,26185], [49875,64694,25971,25976,51096,54914], [26293,76292,76295,57852,76287], [63556,74446,49893,51368,1571,2807,24458], [74445,74448], [34984,34985,34986,39111,50649,51111,55429], [40895,49845], [157,2541,12677,39110,45318,26297], [40746,40747,54915,26262,51357,3917], [40744,40745], [41253,45319,52973,55428,40742,40743], [26167,40831,7825,26757,26759,41251], [17245], [53270,54918,54919,35318,33936,2861,10427], [49870,63272], [45316,55430,31994,33455,41252,41254], [53503], [17244,38832,45308,45317,51754,44626,35343], [40894], [45131,45309,45310,45342,26627,33474,35358], [53505,53506,53507,53508,53509,53510], [45134,45135,45311,43600,43613,43616,53500], [45127,45129], [45124], [45123], [45121], [45119], [45117], [45115], [45112], [45111], [45106], [35357], [35355], [35349], [35341], [35338], [11373], [11370], [35903], [53514], [43615], [43614], [43612], [35334,35347,43607,43609,43610,43611], [51328,51329,51330,51331,51332,51407,51408], [33571,35344,35359,51321,51322,51323], [7709,11929,16286,33562,33563], [43605,43606,43608,45334,36418,42485,3031], [42467,45751,43596,43598,43599], [44553,35336,35337,35345,35346,44574,65369], [35360,35361,42482,42484,42486], [35335,35339,35340,35348,35351,35352,35354], [43589,43590,43592,43593,43594,43595], [43512,45333,45335,45341,63974,45337,45668], [34762,34763,34765,34766,34773,34777,34783], [40089,43513,45304,35650,26395], [63500,34757,34764,34769,34771,34781,34786], [35356,42479,42480,42483,42489,45667,42490], [34775,34779], [34754,34758,34759,34761,34767,34770,34772], [45330,34340,34342], [40893,51403,51404,51488,39342,45328,45329], [52368,45305,65298,34838], [60917,63508,63509,42488,52306,52337], [45307,60373,45306,34444], [35784,36253,38833,38834,38835,36245], [76659,42427,42428,42429,42430,36260], [53146,3855,54739,54740,54578,54579], [51396,52636,58332,42779,42781], [51390,51391,51392,51393,51394,51395], [63505,53119,51387,51388,51389], [65297,44884,45052,45053,63501,63503,63504], [34343,34344,34346,36217,36230,36252], [34338], [54973,54974,58536,36219,26172,34337], [53160,53161], [53153,53154,53155,53156,53157,53158,53159], [53137,53139,53140,53141,53142,53143,53144], [53134,53135], [53128,53129,53130,53131,53132,53133], [53114,53115,53116,53117,53120,53121,53122], [53106,53107], [58345,58346,58347,53104,53105], [58343,58344], [58341,58342], [58340], [58333,58334,58335,58336,58337,58338,58339], [58329,58330], [58322,58323,58324,58325,58326,58327,58328], [52638,52639], [26448,44874,45642,50425,52635,52637], [3866,10451], [26450,26460,26470,37488,37490,45031,45032], [52422,63273,45027,42432,42433,45030], [52420,52421], [52413,52414,52415,52416,52417,52418,52419], [52411,52412], [52406,52407,52408,52409,52410], [52404,52405], [52395,52396,52397,52398,52399,52400,52401], [52391,52392], [52391,52392], [52385,52386,52387,52388,52389,52390], [52383,52384], [52375,52376,52377,52378,52380,52381], [52373,52374], [52365,52366,52367,52369,52370,52371,52372], [52360,52361,52362,52363], [52358,52359], [52351,52352,52353,52354,52355,52356,52357], [52347,52348], [52345,52346], [52342,52343,52344], [52341], [52336,52338,52339,52340], [52334,52335], [52330,52331,52332,52333], [52328,52329], [52323,52324,52325,52326,52327], [52321,52322], [52317,52318,52319,52320], [52313,52314], [52308,52309,52310,52311,52312], [52303,52304,52305,52307], [52301,52302], [52296,52297,52298,52299,52300], [52294,52295], [52288,52289,52290,52291,52292,52293], [36255,52264,52281,52282,52283,52284], [45029,26279], [26466,26468,26469,26471,37489], [26464,26465], [26455,26456,26457,26459,26461,26462], [45026,55112,55113,45028,26449,26453], [57976,57977], [52379,52402,52403,52648,57975], [52315,52316], [45992,45993,45994,45995,45996,45997,45998], [45987], [45979,45980,45981,45982,45983,45984,45986], [45968,45969,45970,45971,45972,45973], [33677,33678,40703,26451,26467,36702], [33670,33671], [33641,33663,33666,33667,33668,33669], [26057,33636], [45320,45321,45322,45323,45324,45325], [34837,34841], [26702,26703,26705,26708,26710,26711,26712], [33652,33653,33654,33655,33656,33657], [33650], [33643,33644,33645,33646,33647,33648,33649], [33634,33635], [33626,33628,33629,33630,33631,33632,33633], [53646,53647,53648,53649,53650,41573], [53644,53645], [33470,33471,33473,42791,51499,51500], [33468,33469], [33456,33457,33458,33465,33467], [33454], [42495,42497,42498,34448,43481,53495], [53965,41581], [34450,41974,52445], [33466,33472], [41578,52455,52634,26682,36709,43150], [26697,26698,26699,26701,26715,26717,41579], [52633,44953], [54938], [15361], [52647], [45055], [45054], [34451], [39856], [15362,39857,34449,34453], [56599,56615,56621,56600,56602]]
#
# url_links = []
# data = []
# counter = 0
# for list in urls:
#     for id in list:
#         url_links.append("https://portalnow.com/es/venta/" + str(id))
#     print(url_links)
#
#     # Almacenar los datos en la lista
#     data.append({
#         "Links": url_links,
#     })
#     # Convertir la lista de datos en un DataFrame
# df = pd.DataFrame(data, columns=['Links'])
# df.to_excel(f"links.xlsx", index=False, engine="openpyxl")
# print(len(url_links))