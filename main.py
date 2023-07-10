
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

url_list =['https://portalnow.com/es/venta/35622', 'https://portalnow.com/es/venta/58174', 'https://portalnow.com/es/venta/26532', 'https://portalnow.com/es/venta/49848', 'https://portalnow.com/es/venta/40755', 'https://portalnow.com/es/venta/50849', 'https://portalnow.com/es/venta/26476', 'https://portalnow.com/es/venta/26197', 'https://portalnow.com/es/venta/51174', 'https://portalnow.com/es/venta/50860', 'https://portalnow.com/es/venta/60427', 'https://portalnow.com/es/venta/26022', 'https://portalnow.com/es/venta/26756', 'https://portalnow.com/es/venta/37996', 'https://portalnow.com/es/venta/53380', 'https://portalnow.com/es/venta/49812', 'https://portalnow.com/es/venta/40187', 'https://portalnow.com/es/venta/26030', 'https://portalnow.com/es/venta/27246', 'https://portalnow.com/es/venta/26896', 'https://portalnow.com/es/venta/53394', 'https://portalnow.com/es/venta/40287', 'https://portalnow.com/es/venta/51545', 'https://portalnow.com/es/venta/26016', 'https://portalnow.com/es/venta/39677', 'https://portalnow.com/es/venta/50515', 'https://portalnow.com/es/venta/51474', 'https://portalnow.com/es/venta/60654', 'https://portalnow.com/es/venta/38283', 'https://portalnow.com/es/venta/26502', 'https://portalnow.com/es/venta/26408', 'https://portalnow.com/es/venta/50780', 'https://portalnow.com/es/venta/76294', 'https://portalnow.com/es/venta/49796', 'https://portalnow.com/es/venta/39006', 'https://portalnow.com/es/venta/26651', 'https://portalnow.com/es/venta/40277', 'https://portalnow.com/es/venta/49912', 'https://portalnow.com/es/venta/26316', 'https://portalnow.com/es/venta/76384', 'https://portalnow.com/es/venta/14745', 'https://portalnow.com/es/venta/26226', 'https://portalnow.com/es/venta/25987', 'https://portalnow.com/es/venta/26915', 'https://portalnow.com/es/venta/40721', 'https://portalnow.com/es/venta/26026', 'https://portalnow.com/es/venta/50748', 'https://portalnow.com/es/venta/59332', 'https://portalnow.com/es/venta/49852', 'https://portalnow.com/es/venta/26763', 'https://portalnow.com/es/venta/31899', 'https://portalnow.com/es/venta/7093', 'https://portalnow.com/es/venta/49786', 'https://portalnow.com/es/venta/54763', 'https://portalnow.com/es/venta/64582', 'https://portalnow.com/es/venta/41126', 'https://portalnow.com/es/venta/60618', 'https://portalnow.com/es/venta/26764', 'https://portalnow.com/es/venta/24878', 'https://portalnow.com/es/venta/55197', 'https://portalnow.com/es/venta/58307', 'https://portalnow.com/es/venta/26739', 'https://portalnow.com/es/venta/40098', 'https://portalnow.com/es/venta/52623', 'https://portalnow.com/es/venta/65107', 'https://portalnow.com/es/venta/74426', 'https://portalnow.com/es/venta/31996', 'https://portalnow.com/es/venta/2528', 'https://portalnow.com/es/venta/49727', 'https://portalnow.com/es/venta/40270', 'https://portalnow.com/es/venta/64243', 'https://portalnow.com/es/venta/39770', 'https://portalnow.com/es/venta/52559', 'https://portalnow.com/es/venta/40868', 'https://portalnow.com/es/venta/14095', 'https://portalnow.com/es/venta/40897', 'https://portalnow.com/es/venta/16254', 'https://portalnow.com/es/venta/50675', 'https://portalnow.com/es/venta/58514', 'https://portalnow.com/es/venta/37596', 'https://portalnow.com/es/venta/26779', 'https://portalnow.com/es/venta/26241', 'https://portalnow.com/es/venta/49849', 'https://portalnow.com/es/venta/61636', 'https://portalnow.com/es/venta/49913', 'https://portalnow.com/es/venta/39113', 'https://portalnow.com/es/venta/50692', 'https://portalnow.com/es/venta/76286', 'https://portalnow.com/es/venta/51463', 'https://portalnow.com/es/venta/26313', 'https://portalnow.com/es/venta/52960', 'https://portalnow.com/es/venta/55585', 'https://portalnow.com/es/venta/40823', 'https://portalnow.com/es/venta/54271', 'https://portalnow.com/es/venta/26742', 'https://portalnow.com/es/venta/51108', 'https://portalnow.com/es/venta/41197', 'https://portalnow.com/es/venta/18747', 'https://portalnow.com/es/venta/9529', 'https://portalnow.com/es/venta/26676', 'https://portalnow.com/es/venta/6260', 'https://portalnow.com/es/venta/17655', 'https://portalnow.com/es/venta/40911', 'https://portalnow.com/es/venta/4510', 'https://portalnow.com/es/venta/7491', 'https://portalnow.com/es/venta/39731', 'https://portalnow.com/es/venta/76288', 'https://portalnow.com/es/venta/2613', 'https://portalnow.com/es/venta/41194', 'https://portalnow.com/es/venta/65697', 'https://portalnow.com/es/venta/18623', 'https://portalnow.com/es/venta/26634', 'https://portalnow.com/es/venta/61500', 'https://portalnow.com/es/venta/64646', 'https://portalnow.com/es/venta/49949', 'https://portalnow.com/es/venta/26566', 'https://portalnow.com/es/venta/2614', 'https://portalnow.com/es/venta/52624', 'https://portalnow.com/es/venta/49806', 'https://portalnow.com/es/venta/39777', 'https://portalnow.com/es/venta/6889', 'https://portalnow.com/es/venta/25982', 'https://portalnow.com/es/venta/51274', 'https://portalnow.com/es/venta/55438', 'https://portalnow.com/es/venta/2844', 'https://portalnow.com/es/venta/21749', 'https://portalnow.com/es/venta/9229', 'https://portalnow.com/es/venta/49884', 'https://portalnow.com/es/venta/26501', 'https://portalnow.com/es/venta/26745', 'https://portalnow.com/es/venta/49813', 'https://portalnow.com/es/venta/26426', 'https://portalnow.com/es/venta/51317', 'https://portalnow.com/es/venta/76315', 'https://portalnow.com/es/venta/40824', 'https://portalnow.com/es/venta/41196', 'https://portalnow.com/es/venta/26633', 'https://portalnow.com/es/venta/49811', 'https://portalnow.com/es/venta/26069', 'https://portalnow.com/es/venta/21734', 'https://portalnow.com/es/venta/16222', 'https://portalnow.com/es/venta/61410', 'https://portalnow.com/es/venta/69', 'https://portalnow.com/es/venta/26578', 'https://portalnow.com/es/venta/49883', 'https://portalnow.com/es/venta/54635', 'https://portalnow.com/es/venta/26580', 'https://portalnow.com/es/venta/50952', 'https://portalnow.com/es/venta/40802', 'https://portalnow.com/es/venta/40716', 'https://portalnow.com/es/venta/26131', 'https://portalnow.com/es/venta/7479', 'https://portalnow.com/es/venta/49916', 'https://portalnow.com/es/venta/52978', 'https://portalnow.com/es/venta/64265', 'https://portalnow.com/es/venta/49862', 'https://portalnow.com/es/venta/50765', 'https://portalnow.com/es/venta/49841', 'https://portalnow.com/es/venta/49765', 'https://portalnow.com/es/venta/50772', 'https://portalnow.com/es/venta/26575', 'https://portalnow.com/es/venta/50682', 'https://portalnow.com/es/venta/2682', 'https://portalnow.com/es/venta/7279', 'https://portalnow.com/es/venta/22493', 'https://portalnow.com/es/venta/2506', 'https://portalnow.com/es/venta/52743', 'https://portalnow.com/es/venta/31695', 'https://portalnow.com/es/venta/49889', 'https://portalnow.com/es/venta/26602', 'https://portalnow.com/es/venta/50695', 'https://portalnow.com/es/venta/38005', 'https://portalnow.com/es/venta/9113', 'https://portalnow.com/es/venta/26428', 'https://portalnow.com/es/venta/31988', 'https://portalnow.com/es/venta/39743', 'https://portalnow.com/es/venta/49730', 'https://portalnow.com/es/venta/49953', 'https://portalnow.com/es/venta/53259', 'https://portalnow.com/es/venta/26550', 'https://portalnow.com/es/venta/51358', 'https://portalnow.com/es/venta/60431', 'https://portalnow.com/es/venta/38004', 'https://portalnow.com/es/venta/49795', 'https://portalnow.com/es/venta/75049', 'https://portalnow.com/es/venta/18182', 'https://portalnow.com/es/venta/49959', 'https://portalnow.com/es/venta/40733', 'https://portalnow.com/es/venta/17817', 'https://portalnow.com/es/venta/49890', 'https://portalnow.com/es/venta/55423', 'https://portalnow.com/es/venta/55581', 'https://portalnow.com/es/venta/24249', 'https://portalnow.com/es/venta/39061', 'https://portalnow.com/es/venta/63741', 'https://portalnow.com/es/venta/49769', 'https://portalnow.com/es/venta/26145', 'https://portalnow.com/es/venta/18460', 'https://portalnow.com/es/venta/20557', 'https://portalnow.com/es/venta/23004', 'https://portalnow.com/es/venta/49762', 'https://portalnow.com/es/venta/21726', 'https://portalnow.com/es/venta/2569', 'https://portalnow.com/es/venta/26379', 'https://portalnow.com/es/venta/39729', 'https://portalnow.com/es/venta/61902', 'https://portalnow.com/es/venta/58320', 'https://portalnow.com/es/venta/49801', 'https://portalnow.com/es/venta/75046', 'https://portalnow.com/es/venta/19290', 'https://portalnow.com/es/venta/24867', 'https://portalnow.com/es/venta/26061', 'https://portalnow.com/es/venta/26749', 'https://portalnow.com/es/venta/31991', 'https://portalnow.com/es/venta/63339', 'https://portalnow.com/es/venta/49834', 'https://portalnow.com/es/venta/60781', 'https://portalnow.com/es/venta/49830', 'https://portalnow.com/es/venta/55424', 'https://portalnow.com/es/venta/2571', 'https://portalnow.com/es/venta/26485', 'https://portalnow.com/es/venta/28922', 'https://portalnow.com/es/venta/25202', 'https://portalnow.com/es/venta/38278', 'https://portalnow.com/es/venta/49761', 'https://portalnow.com/es/venta/21819', 'https://portalnow.com/es/venta/40773', 'https://portalnow.com/es/venta/41199', 'https://portalnow.com/es/venta/26911', 'https://portalnow.com/es/venta/65672', 'https://portalnow.com/es/venta/31757', 'https://portalnow.com/es/venta/60562', 'https://portalnow.com/es/venta/323', 'https://portalnow.com/es/venta/56888', 'https://portalnow.com/es/venta/26132', 'https://portalnow.com/es/venta/40789', 'https://portalnow.com/es/venta/26064', 'https://portalnow.com/es/venta/26728', 'https://portalnow.com/es/venta/51580', 'https://portalnow.com/es/venta/40769', 'https://portalnow.com/es/venta/26574', 'https://portalnow.com/es/venta/40863', 'https://portalnow.com/es/venta/55582', 'https://portalnow.com/es/venta/2664', 'https://portalnow.com/es/venta/51451', 'https://portalnow.com/es/venta/25035', 'https://portalnow.com/es/venta/18452', 'https://portalnow.com/es/venta/21114', 'https://portalnow.com/es/venta/39753', 'https://portalnow.com/es/venta/49839', 'https://portalnow.com/es/venta/10588', 'https://portalnow.com/es/venta/40838', 'https://portalnow.com/es/venta/9140', 'https://portalnow.com/es/venta/52957', 'https://portalnow.com/es/venta/37691', 'https://portalnow.com/es/venta/39090', 'https://portalnow.com/es/venta/50756', 'https://portalnow.com/es/venta/51705', 'https://portalnow.com/es/venta/65066', 'https://portalnow.com/es/venta/62317', 'https://portalnow.com/es/venta/63553', 'https://portalnow.com/es/venta/39772', 'https://portalnow.com/es/venta/39773', 'https://portalnow.com/es/venta/40772', 'https://portalnow.com/es/venta/2640', 'https://portalnow.com/es/venta/25981', 'https://portalnow.com/es/venta/37977', 'https://portalnow.com/es/venta/49919', 'https://portalnow.com/es/venta/19003', 'https://portalnow.com/es/venta/26410', 'https://portalnow.com/es/venta/25196', 'https://portalnow.com/es/venta/49782', 'https://portalnow.com/es/venta/40768', 'https://portalnow.com/es/venta/57019', 'https://portalnow.com/es/venta/49760', 'https://portalnow.com/es/venta/20830', 'https://portalnow.com/es/venta/39734', 'https://portalnow.com/es/venta/14064', 'https://portalnow.com/es/venta/21820', 'https://portalnow.com/es/venta/40803', 'https://portalnow.com/es/venta/26743', 'https://portalnow.com/es/venta/23395', 'https://portalnow.com/es/venta/53757', 'https://portalnow.com/es/venta/18209', 'https://portalnow.com/es/venta/75039', 'https://portalnow.com/es/venta/26568', 'https://portalnow.com/es/venta/1064', 'https://portalnow.com/es/venta/40898', 'https://portalnow.com/es/venta/39518', 'https://portalnow.com/es/venta/8101', 'https://portalnow.com/es/venta/11485', 'https://portalnow.com/es/venta/20494', 'https://portalnow.com/es/venta/26667', 'https://portalnow.com/es/venta/55937', 'https://portalnow.com/es/venta/51233', 'https://portalnow.com/es/venta/26194', 'https://portalnow.com/es/venta/40714', 'https://portalnow.com/es/venta/3580', 'https://portalnow.com/es/venta/20951', 'https://portalnow.com/es/venta/63985', 'https://portalnow.com/es/venta/26490', 'https://portalnow.com/es/venta/65242', 'https://portalnow.com/es/venta/51377', 'https://portalnow.com/es/venta/25030', 'https://portalnow.com/es/venta/40882', 'https://portalnow.com/es/venta/55583', 'https://portalnow.com/es/venta/65129', 'https://portalnow.com/es/venta/55337', 'https://portalnow.com/es/venta/3584', 'https://portalnow.com/es/venta/49742', 'https://portalnow.com/es/venta/52054', 'https://portalnow.com/es/venta/61540', 'https://portalnow.com/es/venta/49879', 'https://portalnow.com/es/venta/26427', 'https://portalnow.com/es/venta/40899', 'https://portalnow.com/es/venta/39244', 'https://portalnow.com/es/venta/40930', 'https://portalnow.com/es/venta/50602', 'https://portalnow.com/es/venta/50690', 'https://portalnow.com/es/venta/24233', 'https://portalnow.com/es/venta/26195', 'https://portalnow.com/es/venta/64565', 'https://portalnow.com/es/venta/1598', 'https://portalnow.com/es/venta/24566', 'https://portalnow.com/es/venta/26244', 'https://portalnow.com/es/venta/49869', 'https://portalnow.com/es/venta/26029', 'https://portalnow.com/es/venta/2659', 'https://portalnow.com/es/venta/40801', 'https://portalnow.com/es/venta/49898', 'https://portalnow.com/es/venta/74938', 'https://portalnow.com/es/venta/40669', 'https://portalnow.com/es/venta/49754', 'https://portalnow.com/es/venta/19112', 'https://portalnow.com/es/venta/34576', 'https://portalnow.com/es/venta/51461', 'https://portalnow.com/es/venta/612', 'https://portalnow.com/es/venta/41203', 'https://portalnow.com/es/venta/55580', 'https://portalnow.com/es/venta/9126', 'https://portalnow.com/es/venta/26027', 'https://portalnow.com/es/venta/50694', 'https://portalnow.com/es/venta/63548', 'https://portalnow.com/es/venta/28997', 'https://portalnow.com/es/venta/51776', 'https://portalnow.com/es/venta/9069', 'https://portalnow.com/es/venta/26298', 'https://portalnow.com/es/venta/51752', 'https://portalnow.com/es/venta/26505', 'https://portalnow.com/es/venta/2418', 'https://portalnow.com/es/venta/8953', 'https://portalnow.com/es/venta/26618', 'https://portalnow.com/es/venta/26683', 'https://portalnow.com/es/venta/49785', 'https://portalnow.com/es/venta/50752', 'https://portalnow.com/es/venta/17837', 'https://portalnow.com/es/venta/2705', 'https://portalnow.com/es/venta/11655', 'https://portalnow.com/es/venta/12592', 'https://portalnow.com/es/venta/51479', 'https://portalnow.com/es/venta/61594', 'https://portalnow.com/es/venta/25979', 'https://portalnow.com/es/venta/23817', 'https://portalnow.com/es/venta/55348', 'https://portalnow.com/es/venta/26001', 'https://portalnow.com/es/venta/2781', 'https://portalnow.com/es/venta/9032', 'https://portalnow.com/es/venta/49807', 'https://portalnow.com/es/venta/51584', 'https://portalnow.com/es/venta/75056', 'https://portalnow.com/es/venta/26294', 'https://portalnow.com/es/venta/49892', 'https://portalnow.com/es/venta/26497', 'https://portalnow.com/es/venta/25308', 'https://portalnow.com/es/venta/2854', 'https://portalnow.com/es/venta/8135', 'https://portalnow.com/es/venta/4470', 'https://portalnow.com/es/venta/7081', 'https://portalnow.com/es/venta/26129', 'https://portalnow.com/es/venta/26531', 'https://portalnow.com/es/venta/51477', 'https://portalnow.com/es/venta/61909', 'https://portalnow.com/es/venta/29035', 'https://portalnow.com/es/venta/49851', 'https://portalnow.com/es/venta/8807', 'https://portalnow.com/es/venta/26403', 'https://portalnow.com/es/venta/40072', 'https://portalnow.com/es/venta/26117', 'https://portalnow.com/es/venta/55349', 'https://portalnow.com/es/venta/25998', 'https://portalnow.com/es/venta/49810', 'https://portalnow.com/es/venta/63369', 'https://portalnow.com/es/venta/1522', 'https://portalnow.com/es/venta/24376', 'https://portalnow.com/es/venta/26134', 'https://portalnow.com/es/venta/38277', 'https://portalnow.com/es/venta/50768', 'https://portalnow.com/es/venta/58589', 'https://portalnow.com/es/venta/40748', 'https://portalnow.com/es/venta/61519', 'https://portalnow.com/es/venta/40852', 'https://portalnow.com/es/venta/51376', 'https://portalnow.com/es/venta/13495', 'https://portalnow.com/es/venta/26295', 'https://portalnow.com/es/venta/26311', 'https://portalnow.com/es/venta/40926', 'https://portalnow.com/es/venta/65462', 'https://portalnow.com/es/venta/53449', 'https://portalnow.com/es/venta/26004', 'https://portalnow.com/es/venta/4467', 'https://portalnow.com/es/venta/50420', 'https://portalnow.com/es/venta/60649', 'https://portalnow.com/es/venta/28928', 'https://portalnow.com/es/venta/24265', 'https://portalnow.com/es/venta/26169', 'https://portalnow.com/es/venta/26746', 'https://portalnow.com/es/venta/49923', 'https://portalnow.com/es/venta/24247', 'https://portalnow.com/es/venta/61670', 'https://portalnow.com/es/venta/576', 'https://portalnow.com/es/venta/9692', 'https://portalnow.com/es/venta/26430', 'https://portalnow.com/es/venta/49824', 'https://portalnow.com/es/venta/26128', 'https://portalnow.com/es/venta/26304', 'https://portalnow.com/es/venta/40737', 'https://portalnow.com/es/venta/66038', 'https://portalnow.com/es/venta/26597', 'https://portalnow.com/es/venta/41193', 'https://portalnow.com/es/venta/3824', 'https://portalnow.com/es/venta/14627', 'https://portalnow.com/es/venta/21056', 'https://portalnow.com/es/venta/21152', 'https://portalnow.com/es/venta/26524', 'https://portalnow.com/es/venta/26124', 'https://portalnow.com/es/venta/26243', 'https://portalnow.com/es/venta/26420', 'https://portalnow.com/es/venta/26641', 'https://portalnow.com/es/venta/39735', 'https://portalnow.com/es/venta/13269', 'https://portalnow.com/es/venta/26122', 'https://portalnow.com/es/venta/23002', 'https://portalnow.com/es/venta/25986', 'https://portalnow.com/es/venta/61903', 'https://portalnow.com/es/venta/26778', 'https://portalnow.com/es/venta/25994', 'https://portalnow.com/es/venta/25995', 'https://portalnow.com/es/venta/49902', 'https://portalnow.com/es/venta/63275', 'https://portalnow.com/es/venta/49922', 'https://portalnow.com/es/venta/64537', 'https://portalnow.com/es/venta/76201', 'https://portalnow.com/es/venta/25980', 'https://portalnow.com/es/venta/26567', 'https://portalnow.com/es/venta/52856', 'https://portalnow.com/es/venta/58318', 'https://portalnow.com/es/venta/40917', 'https://portalnow.com/es/venta/53466', 'https://portalnow.com/es/venta/24251', 'https://portalnow.com/es/venta/1056', 'https://portalnow.com/es/venta/26444', 'https://portalnow.com/es/venta/26669', 'https://portalnow.com/es/venta/40667', 'https://portalnow.com/es/venta/26115', 'https://portalnow.com/es/venta/39764', 'https://portalnow.com/es/venta/6857', 'https://portalnow.com/es/venta/12810', 'https://portalnow.com/es/venta/26323', 'https://portalnow.com/es/venta/26643', 'https://portalnow.com/es/venta/40928', 'https://portalnow.com/es/venta/49766', 'https://portalnow.com/es/venta/54954', 'https://portalnow.com/es/venta/11463', 'https://portalnow.com/es/venta/18461', 'https://portalnow.com/es/venta/21805', 'https://portalnow.com/es/venta/23393', 'https://portalnow.com/es/venta/26325', 'https://portalnow.com/es/venta/56073', 'https://portalnow.com/es/venta/63277', 'https://portalnow.com/es/venta/40836', 'https://portalnow.com/es/venta/75044', 'https://portalnow.com/es/venta/40905', 'https://portalnow.com/es/venta/84', 'https://portalnow.com/es/venta/8094', 'https://portalnow.com/es/venta/21199', 'https://portalnow.com/es/venta/41204', 'https://portalnow.com/es/venta/1686', 'https://portalnow.com/es/venta/8308', 'https://portalnow.com/es/venta/53263', 'https://portalnow.com/es/venta/64206', 'https://portalnow.com/es/venta/40903', 'https://portalnow.com/es/venta/40908', 'https://portalnow.com/es/venta/12343', 'https://portalnow.com/es/venta/26576', 'https://portalnow.com/es/venta/74802', 'https://portalnow.com/es/venta/54613', 'https://portalnow.com/es/venta/40687', 'https://portalnow.com/es/venta/18546', 'https://portalnow.com/es/venta/52959', 'https://portalnow.com/es/venta/915', 'https://portalnow.com/es/venta/2536', 'https://portalnow.com/es/venta/6917', 'https://portalnow.com/es/venta/13707', 'https://portalnow.com/es/venta/15644', 'https://portalnow.com/es/venta/64644', 'https://portalnow.com/es/venta/10524', 'https://portalnow.com/es/venta/52562', 'https://portalnow.com/es/venta/26493', 'https://portalnow.com/es/venta/7295', 'https://portalnow.com/es/venta/7478', 'https://portalnow.com/es/venta/7761', 'https://portalnow.com/es/venta/39742', 'https://portalnow.com/es/venta/18046', 'https://portalnow.com/es/venta/16272', 'https://portalnow.com/es/venta/49856', 'https://portalnow.com/es/venta/50638', 'https://portalnow.com/es/venta/52493', 'https://portalnow.com/es/venta/61803', 'https://portalnow.com/es/venta/26245', 'https://portalnow.com/es/venta/26590', 'https://portalnow.com/es/venta/26740', 'https://portalnow.com/es/venta/28921', 'https://portalnow.com/es/venta/50762', 'https://portalnow.com/es/venta/14051', 'https://portalnow.com/es/venta/14072', 'https://portalnow.com/es/venta/10507', 'https://portalnow.com/es/venta/49911', 'https://portalnow.com/es/venta/64130', 'https://portalnow.com/es/venta/76672', 'https://portalnow.com/es/venta/26478', 'https://portalnow.com/es/venta/66209', 'https://portalnow.com/es/venta/26070', 'https://portalnow.com/es/venta/6793', 'https://portalnow.com/es/venta/26663', 'https://portalnow.com/es/venta/37926', 'https://portalnow.com/es/venta/40924', 'https://portalnow.com/es/venta/49780', 'https://portalnow.com/es/venta/49790', 'https://portalnow.com/es/venta/26251', 'https://portalnow.com/es/venta/55387', 'https://portalnow.com/es/venta/40070', 'https://portalnow.com/es/venta/40693', 'https://portalnow.com/es/venta/40813', 'https://portalnow.com/es/venta/49831', 'https://portalnow.com/es/venta/57130', 'https://portalnow.com/es/venta/74940', 'https://portalnow.com/es/venta/51445', 'https://portalnow.com/es/venta/1307', 'https://portalnow.com/es/venta/18160', 'https://portalnow.com/es/venta/26521', 'https://portalnow.com/es/venta/40933', 'https://portalnow.com/es/venta/75047', 'https://portalnow.com/es/venta/26074', 'https://portalnow.com/es/venta/26077', 'https://portalnow.com/es/venta/49767', 'https://portalnow.com/es/venta/40675', 'https://portalnow.com/es/venta/26068', 'https://portalnow.com/es/venta/26076', 'https://portalnow.com/es/venta/39712', 'https://portalnow.com/es/venta/52873', 'https://portalnow.com/es/venta/3046', 'https://portalnow.com/es/venta/20042', 'https://portalnow.com/es/venta/25048', 'https://portalnow.com/es/venta/52870', 'https://portalnow.com/es/venta/63276', 'https://portalnow.com/es/venta/49948', 'https://portalnow.com/es/venta/52671', 'https://portalnow.com/es/venta/26110', 'https://portalnow.com/es/venta/26307', 'https://portalnow.com/es/venta/52056', 'https://portalnow.com/es/venta/26066', 'https://portalnow.com/es/venta/26116', 'https://portalnow.com/es/venta/26496', 'https://portalnow.com/es/venta/58414', 'https://portalnow.com/es/venta/3583', 'https://portalnow.com/es/venta/51927', 'https://portalnow.com/es/venta/26072', 'https://portalnow.com/es/venta/66210', 'https://portalnow.com/es/venta/9153', 'https://portalnow.com/es/venta/26709', 'https://portalnow.com/es/venta/39165', 'https://portalnow.com/es/venta/40931', 'https://portalnow.com/es/venta/49918', 'https://portalnow.com/es/venta/51164', 'https://portalnow.com/es/venta/52857', 'https://portalnow.com/es/venta/13315', 'https://portalnow.com/es/venta/23812', 'https://portalnow.com/es/venta/24660', 'https://portalnow.com/es/venta/26109', 'https://portalnow.com/es/venta/26113', 'https://portalnow.com/es/venta/3852', 'https://portalnow.com/es/venta/26071', 'https://portalnow.com/es/venta/26067', 'https://portalnow.com/es/venta/61897', 'https://portalnow.com/es/venta/39739', 'https://portalnow.com/es/venta/53262', 'https://portalnow.com/es/venta/50693', 'https://portalnow.com/es/venta/40822', 'https://portalnow.com/es/venta/49800', 'https://portalnow.com/es/venta/49878', 'https://portalnow.com/es/venta/55192', 'https://portalnow.com/es/venta/60704', 'https://portalnow.com/es/venta/26414', 'https://portalnow.com/es/venta/24256', 'https://portalnow.com/es/venta/26525', 'https://portalnow.com/es/venta/40796', 'https://portalnow.com/es/venta/54905', 'https://portalnow.com/es/venta/76614', 'https://portalnow.com/es/venta/63336', 'https://portalnow.com/es/venta/60771', 'https://portalnow.com/es/venta/2808', 'https://portalnow.com/es/venta/13485', 'https://portalnow.com/es/venta/26296', 'https://portalnow.com/es/venta/26250', 'https://portalnow.com/es/venta/39678', 'https://portalnow.com/es/venta/40887', 'https://portalnow.com/es/venta/49840', 'https://portalnow.com/es/venta/76654', 'https://portalnow.com/es/venta/54833', 'https://portalnow.com/es/venta/334', 'https://portalnow.com/es/venta/2566', 'https://portalnow.com/es/venta/16256', 'https://portalnow.com/es/venta/20644', 'https://portalnow.com/es/venta/26570', 'https://portalnow.com/es/venta/26640', 'https://portalnow.com/es/venta/51234', 'https://portalnow.com/es/venta/39759', 'https://portalnow.com/es/venta/53451', 'https://portalnow.com/es/venta/52963', 'https://portalnow.com/es/venta/53676', 'https://portalnow.com/es/venta/54884', 'https://portalnow.com/es/venta/56230', 'https://portalnow.com/es/venta/40800', 'https://portalnow.com/es/venta/2864', 'https://portalnow.com/es/venta/13700', 'https://portalnow.com/es/venta/40841', 'https://portalnow.com/es/venta/49738', 'https://portalnow.com/es/venta/51578', 'https://portalnow.com/es/venta/52859', 'https://portalnow.com/es/venta/40668', 'https://portalnow.com/es/venta/26249', 'https://portalnow.com/es/venta/39740', 'https://portalnow.com/es/venta/38003', 'https://portalnow.com/es/venta/40938', 'https://portalnow.com/es/venta/54909', 'https://portalnow.com/es/venta/40853', 'https://portalnow.com/es/venta/3772', 'https://portalnow.com/es/venta/25988', 'https://portalnow.com/es/venta/17120', 'https://portalnow.com/es/venta/17182', 'https://portalnow.com/es/venta/17257', 'https://portalnow.com/es/venta/17834', 'https://portalnow.com/es/venta/18449', 'https://portalnow.com/es/venta/18698', 'https://portalnow.com/es/venta/22554', 'https://portalnow.com/es/venta/26760', 'https://portalnow.com/es/venta/40855', 'https://portalnow.com/es/venta/64066', 'https://portalnow.com/es/venta/13698', 'https://portalnow.com/es/venta/15639', 'https://portalnow.com/es/venta/15656', 'https://portalnow.com/es/venta/19136', 'https://portalnow.com/es/venta/26434', 'https://portalnow.com/es/venta/26504', 'https://portalnow.com/es/venta/7879', 'https://portalnow.com/es/venta/51484', 'https://portalnow.com/es/venta/85', 'https://portalnow.com/es/venta/12996', 'https://portalnow.com/es/venta/22370', 'https://portalnow.com/es/venta/40806', 'https://portalnow.com/es/venta/52863', 'https://portalnow.com/es/venta/76383', 'https://portalnow.com/es/venta/26489', 'https://portalnow.com/es/venta/19569', 'https://portalnow.com/es/venta/23822', 'https://portalnow.com/es/venta/26734', 'https://portalnow.com/es/venta/49803', 'https://portalnow.com/es/venta/9163', 'https://portalnow.com/es/venta/18457', 'https://portalnow.com/es/venta/18658', 'https://portalnow.com/es/venta/18659', 'https://portalnow.com/es/venta/41259', 'https://portalnow.com/es/venta/26003', 'https://portalnow.com/es/venta/49880', 'https://portalnow.com/es/venta/40856', 'https://portalnow.com/es/venta/41258', 'https://portalnow.com/es/venta/26153', 'https://portalnow.com/es/venta/26154', 'https://portalnow.com/es/venta/26402', 'https://portalnow.com/es/venta/26767', 'https://portalnow.com/es/venta/38760', 'https://portalnow.com/es/venta/39762', 'https://portalnow.com/es/venta/26645', 'https://portalnow.com/es/venta/26751', 'https://portalnow.com/es/venta/49726', 'https://portalnow.com/es/venta/49775', 'https://portalnow.com/es/venta/58302', 'https://portalnow.com/es/venta/39733', 'https://portalnow.com/es/venta/26446', 'https://portalnow.com/es/venta/26582', 'https://portalnow.com/es/venta/83', 'https://portalnow.com/es/venta/75057', 'https://portalnow.com/es/venta/64219', 'https://portalnow.com/es/venta/3920', 'https://portalnow.com/es/venta/5198', 'https://portalnow.com/es/venta/12766', 'https://portalnow.com/es/venta/26156', 'https://portalnow.com/es/venta/6818', 'https://portalnow.com/es/venta/6963', 'https://portalnow.com/es/venta/50750', 'https://portalnow.com/es/venta/50777', 'https://portalnow.com/es/venta/61633', 'https://portalnow.com/es/venta/18898', 'https://portalnow.com/es/venta/39760', 'https://portalnow.com/es/venta/58417', 'https://portalnow.com/es/venta/1545', 'https://portalnow.com/es/venta/39748', 'https://portalnow.com/es/venta/26130', 'https://portalnow.com/es/venta/53453', 'https://portalnow.com/es/venta/51367', 'https://portalnow.com/es/venta/52974', 'https://portalnow.com/es/venta/54925', 'https://portalnow.com/es/venta/40706', 'https://portalnow.com/es/venta/26463', 'https://portalnow.com/es/venta/26491', 'https://portalnow.com/es/venta/31992', 'https://portalnow.com/es/venta/32137', 'https://portalnow.com/es/venta/39749', 'https://portalnow.com/es/venta/40814', 'https://portalnow.com/es/venta/40872', 'https://portalnow.com/es/venta/49903', 'https://portalnow.com/es/venta/53463', 'https://portalnow.com/es/venta/56560', 'https://portalnow.com/es/venta/63258', 'https://portalnow.com/es/venta/26612', 'https://portalnow.com/es/venta/53450', 'https://portalnow.com/es/venta/6667', 'https://portalnow.com/es/venta/26158', 'https://portalnow.com/es/venta/26171', 'https://portalnow.com/es/venta/26211', 'https://portalnow.com/es/venta/26383', 'https://portalnow.com/es/venta/53461', 'https://portalnow.com/es/venta/58692', 'https://portalnow.com/es/venta/32134', 'https://portalnow.com/es/venta/37457', 'https://portalnow.com/es/venta/40804', 'https://portalnow.com/es/venta/49823', 'https://portalnow.com/es/venta/50771', 'https://portalnow.com/es/venta/52854', 'https://portalnow.com/es/venta/53460', 'https://portalnow.com/es/venta/31755', 'https://portalnow.com/es/venta/6897', 'https://portalnow.com/es/venta/26458', 'https://portalnow.com/es/venta/26898', 'https://portalnow.com/es/venta/26899', 'https://portalnow.com/es/venta/26902', 'https://portalnow.com/es/venta/26904', 'https://portalnow.com/es/venta/39745', 'https://portalnow.com/es/venta/40842', 'https://portalnow.com/es/venta/51596', 'https://portalnow.com/es/venta/53462', 'https://portalnow.com/es/venta/55835', 'https://portalnow.com/es/venta/49832', 'https://portalnow.com/es/venta/49846', 'https://portalnow.com/es/venta/40896', 'https://portalnow.com/es/venta/40932', 'https://portalnow.com/es/venta/41228', 'https://portalnow.com/es/venta/41233', 'https://portalnow.com/es/venta/41243', 'https://portalnow.com/es/venta/41245', 'https://portalnow.com/es/venta/38281', 'https://portalnow.com/es/venta/40808', 'https://portalnow.com/es/venta/26136', 'https://portalnow.com/es/venta/26151', 'https://portalnow.com/es/venta/26322', 'https://portalnow.com/es/venta/26378', 'https://portalnow.com/es/venta/28949', 'https://portalnow.com/es/venta/38010', 'https://portalnow.com/es/venta/26646', 'https://portalnow.com/es/venta/29001', 'https://portalnow.com/es/venta/26161', 'https://portalnow.com/es/venta/26235', 'https://portalnow.com/es/venta/26247', 'https://portalnow.com/es/venta/26315', 'https://portalnow.com/es/venta/26512', 'https://portalnow.com/es/venta/26571', 'https://portalnow.com/es/venta/40864', 'https://portalnow.com/es/venta/40890', 'https://portalnow.com/es/venta/8947', 'https://portalnow.com/es/venta/18189', 'https://portalnow.com/es/venta/26268', 'https://portalnow.com/es/venta/26399', 'https://portalnow.com/es/venta/29216', 'https://portalnow.com/es/venta/39725', 'https://portalnow.com/es/venta/40730', 'https://portalnow.com/es/venta/40735', 'https://portalnow.com/es/venta/40927', 'https://portalnow.com/es/venta/50685', 'https://portalnow.com/es/venta/60028', 'https://portalnow.com/es/venta/40749', 'https://portalnow.com/es/venta/26024', 'https://portalnow.com/es/venta/39775', 'https://portalnow.com/es/venta/26237', 'https://portalnow.com/es/venta/26637', 'https://portalnow.com/es/venta/49797', 'https://portalnow.com/es/venta/60370', 'https://portalnow.com/es/venta/58278', 'https://portalnow.com/es/venta/60501', 'https://portalnow.com/es/venta/127', 'https://portalnow.com/es/venta/355', 'https://portalnow.com/es/venta/9097', 'https://portalnow.com/es/venta/14594', 'https://portalnow.com/es/venta/17768', 'https://portalnow.com/es/venta/37454', 'https://portalnow.com/es/venta/158', 'https://portalnow.com/es/venta/229', 'https://portalnow.com/es/venta/3755', 'https://portalnow.com/es/venta/7089', 'https://portalnow.com/es/venta/8250', 'https://portalnow.com/es/venta/52971', 'https://portalnow.com/es/venta/53456']
#
data = []
counter = 0
for url in url_list:

    driver.get(url)
    time.sleep(10)

    accept_cookies_button_locator = (
    By.CSS_SELECTOR, "#infocookie > p:nth-child(3) > a.btn.btn-primary.btn-sm.btn-cookie.mr-3")
    try:
        wait = WebDriverWait(driver, 20)
        accept_cookies_button = wait.until(EC.element_to_be_clickable(accept_cookies_button_locator))
        accept_cookies_button.click()
    except (TimeoutException, NoSuchElementException):
        print("No se pudo hacer clic en el botón de aceptar cookies o el elemento no está presente")

    # # Esperar a que el elemento esté presente en la página antes de extraer el texto
    # wait = WebDriverWait(driver, 10)


    wait = WebDriverWait(driver, 40)

    # provincia
    try:
        provincia_element = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/pn-root/pn-navigation/mat-sidenav-container/mat-sidenav-content/pn-asset-detail/div/div[1]/div[1]/div[2]")))

        provincia_text = provincia_element.text
        words = provincia_text.split(",")  # divide la cadena en palabras usando la coma como separador
        first_word = words[1]  # accede a la primera palabra antes de la coma
    except TimeoutException:
        first_word = 'N/A'

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
        main_photo_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='swiper-wrapper-11b10e45faf688495']/div[1]/pn-responsive-image/picture/img")))
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
    print(f'ref: {referencia_text}, title: {title_text}, description: {descripcion_text}, metros: {metros_text}, hab: {dormitorio_text}, baños: {bano_text}, price: {price_text}, provincia: {first_word},´img: {image_source}')

    # Almacenar los datos en la lista
    data.append({
        "Referencia": referencia_text,
        "Title": title_text,
        "Descripcion": descripcion_text,
        "Provincia": first_word,
        "MetrosCuadrados": metros_text,
        "Dormitorios": dormitorio_text,
        "Baños": bano_text,
        "Price": price_text,
        "MainPhoto": image_source,


    })

    # Convertir la lista de datos en un DataFrame
    df = pd.DataFrame(data, columns=['Referencia', 'Title', 'Descripcion', 'MetrosCuadrados', 'Dormitorios', 'Baños', 'Price', 'MainPhoto', 'Provincia'])


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