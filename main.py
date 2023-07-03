
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
#
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
#
# # url_list = ["https://www.solvia.es/es/propiedades/comprar/piso-barcelona-2-dormitorio-110833-174829",
# #             "https://www.solvia.es/es/propiedades/comprar/piso-bell-lloc-durgell-2-dormitorio-71710-157304",
# #             "https://www.solvia.es/es/propiedades/comprar/piso-monovar-monover-3-dormitorio-93893-119688"]
#
# data = []
# counter = 0
# for url in url_list:
#
#     driver.get(url)
#     time.sleep(10)
#
#     accept_cookies_button_locator = (
#     By.CSS_SELECTOR, "#infocookie > p:nth-child(3) > a.btn.btn-primary.btn-sm.btn-cookie.mr-3")
#     try:
#         wait = WebDriverWait(driver, 20)
#         accept_cookies_button = wait.until(EC.element_to_be_clickable(accept_cookies_button_locator))
#         accept_cookies_button.click()
#     except (TimeoutException, NoSuchElementException):
#         print("No se pudo hacer clic en el botón de aceptar cookies o el elemento no está presente")
#
#     # # Esperar a que el elemento esté presente en la página antes de extraer el texto
#     # wait = WebDriverWait(driver, 10)
#
#
#     wait = WebDriverWait(driver, 40)
#
#     # provincia
#     try:
#         provincia_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='ficha']/h1")))
#         provincia_text = provincia_element.text
#         words = provincia_text.split()  # divide la cadena en palabras
#         last_province = words[-1]  # accede a la última palabra
#     except TimeoutException:
#         last_province = 'N/A'
#
#     # Metros cuadrados
#     try:
#         metros_element = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//*[@id='ficha']/div[3]/div[2]/ul/li[2]")))
#         metros_text = metros_element.text
#         metros_text = metros_text.replace("Superficie:", "")
#     except TimeoutException:
#         metros_text = 'N/A'
#
#     # Dormitorios
#     try:
#         dormitorio_element = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='ficha']/div[3]/div[2]/ul/li[3]")))
#         dormitorio_text = dormitorio_element.text
#         dormitorio_text = dormitorio_text.replace("Nº habitaciones:", "")
#     except TimeoutException:
#         dormitorio_text = 'N/A'
#
#     # Baños
#     try:
#         bano_element = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='ficha']/div[3]/div[2]/ul/li[4]")))
#         bano_text = bano_element.text
#         bano_text = bano_text.replace("Baños:", "")
#     except TimeoutException:
#         bano_text = 'N/A'
#
#
#     # Referencia
#     try:
#         referencia_element = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='ficha']/p[2]/span")))
#         referencia_text = referencia_element.text
#     except TimeoutException:
#         referencia_text = 'N/A'
#
#
#     # Título
#     try:
#         title_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='ficha']/h1")))
#         title_text = title_element.text
#     except:
#         title_text = 'N/A'
#
#
#     # Descripción
#     try:
#         descripcion_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='ficha']/p[1]")))
#         descripcion_text = descripcion_element.text
#     except:
#         descripcion_text = 'N/A'
#
#     # Precio
#     try:
#         price_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='ficha']/div[1]/div/div[2]/div[2]")))
#         price_text = price_element.text
#     except:
#         price_text = 'N/A'
#
#     # Imagen principal
#     try:
#         main_photo_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='carousel-img-detail']/img")))
#         image_source = main_photo_element.get_attribute("src")
#     except:
#         image_source = 'N/A'
#
#     #ImageSources
#     try:
#         image_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='row']/div/div/img")))
#         image_sources = [img.get_attribute("src") for img in image_elements]
#     except:
#         image_sources = 'N/A'
#
#     #imprimir todos los valores por consola
#     print(f'ref: {referencia_text}, title: {title_text}, description: {descripcion_text}, metros: {metros_text}, hab: {dormitorio_text}, baños: {bano_text}, price: {price_text}, provincia: {last_province},´img: {image_source}, imgs: {image_sources}')
#
#     # Almacenar los datos en la lista
#     data.append({
#         "Referencia": referencia_text,
#         "Title": title_text,
#         "Descripcion": descripcion_text,
#         "Provincia": last_province,
#         "MetrosCuadrados": metros_text,
#         "Dormitorios": dormitorio_text,
#         "Baños": bano_text,
#         "Price": price_text,
#         "MainPhoto": image_source,
#         "ImageSources": image_sources
#
#     })
#
#     # Convertir la lista de datos en un DataFrame
#     df = pd.DataFrame(data, columns=['Referencia', 'Title', 'Descripcion', 'MetrosCuadrados', 'Dormitorios', 'Baños', 'Price', 'MainPhoto', 'Provincia', 'ImageSources'])
#
#
#     if counter % 20 == 0:
#         file_counter = counter // 20
#
#         df.to_excel(f"properties_data_{file_counter}.xlsx", index=False, engine="openpyxl")
#
# driver.quit()




import json
import xml.etree.ElementTree as ET
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import date
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el navegador
driver = webdriver.Chrome()

# Lee el archivo Excel y obtiene los URLs de la columna "Referencia"
df = pd.read_excel('enlaces_vivantial.xlsx', sheet_name='Sheet1', usecols=['link'])

# Convierte los URLs en una lista
url_list = df['link'].tolist()

data = []
counter = 0

try:
    for url in url_list:
        driver.get(url)
        time.sleep(10)

        accept_cookies_button_locator = (By.CSS_SELECTOR, "#infocookie > p:nth-child(3) > a.btn.btn-primary.btn-sm.btn-cookie.mr-3")
        try:
            wait = WebDriverWait(driver, 20)
            accept_cookies_button = wait.until(EC.element_to_be_clickable(accept_cookies_button_locator))
            accept_cookies_button.click()
        except (TimeoutException, NoSuchElementException):
            print("No se pudo hacer clic en el botón de aceptar cookies o el elemento no está presente")

        wait = WebDriverWait(driver, 40)

        # provincia
        try:
            provincia_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='ficha']/h1")))
            provincia_text = provincia_element.text
            words = provincia_text.split()  # divide la cadena en palabras
            last_province = words[-1]  # accede a la última palabra
        except TimeoutException:
            last_province = 'N/A'

        # Metros cuadrados
        try:
            metros_element = wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='ficha']/div[3]/div[2]/ul/li[2]")))
            metros_text = metros_element.text
            metros_text = metros_text.replace("Superficie:", "")
        except TimeoutException:
            metros_text = 'N/A'

        # Dormitorios
        try:
            dormitorio_element = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='ficha']/div[3]/div[2]/ul/li[3]")))
            dormitorio_text = dormitorio_element.text
            dormitorio_text = dormitorio_text.replace("Nº habitaciones:", "")
        except TimeoutException:
            dormitorio_text = 'N/A'

        # Baños
        try:
            bano_element = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='ficha']/div[3]/div[2]/ul/li[4]")))
            bano_text = bano_element.text
            bano_text = bano_text.replace("Baños:", "")
        except TimeoutException:
            bano_text = 'N/A'

        # Referencia
        try:
            referencia_element = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='ficha']/p[2]/span")))
            referencia_text = referencia_element.text
        except TimeoutException:
            referencia_text = 'N/A'

        # Título
        try:
            title_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='ficha']/h1")))
            title_text = title_element.text
        except:
            title_text = 'N/A'

        # Descripción
        try:
            descripcion_element = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='ficha']/div[2]/div/div")))
            descripcion_text = descripcion_element.text
        except TimeoutException:
            descripcion_text = 'N/A'

        data.append([last_province, metros_text, dormitorio_text, bano_text, referencia_text, title_text, descripcion_text])

except WebDriverException:
    driver.quit()
    driver = webdriver.Chrome()
    # Aquí podrías intentar realizar la acción que falló nuevamente o continuar con el siguiente URL

driver.quit()

df = pd.DataFrame(data, columns=["Provincia", "Metros cuadrados", "Dormitorios", "Baños", "Referencia", "Título", "Descripción"])
df.to_csv('datos_vivanti.csv', index=False, encoding='utf-8')
