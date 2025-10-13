import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def extrair_inteiro(texto):
	try:
		i = texto.rindex(' ')
		sem_unidade = texto[:i]

		# Às vezes, esse valor pode iniciar pelo ano...
		i = sem_unidade.find(' ')
		if i >= 0:
			sem_unidade = sem_unidade[(i + 1):]

		sem_virgula = sem_unidade.replace(',', '')

		return int(sem_virgula)
	except:
		return 0

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # mantém o Chrome aberto após o script
driver = webdriver.Chrome(options=options)
driver.get('https://www.google.com')

# Tenta aceitar o banner de consentimento do Google (quando existir)
def aceitar_consentimento_google(driver, timeout=6):
	try:
		# Alguns fluxos exibem um iframe de consentimento
		WebDriverWait(driver, timeout).until(
			EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[src*="consent.google.com"], iframe[title*="consent" i], iframe[name^="__"], iframe[id^="__"]'))
		)
		try:
			# Possíveis seletores de botões (pt/en) dentro do iframe
			possiveis_botoes = [
				'button[aria-label="Aceitar tudo" i]',
				'button[aria-label*="Aceitar" i]',
				'button[aria-label="Accept all" i]',
				'#L2AGLb',  # às vezes usado pelo Google
				'button#introAgreeButton',
			]
			for sel in possiveis_botoes:
				try:
					btn = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, sel)))
					btn.click()
					break
				except TimeoutException:
					continue
		finally:
			driver.switch_to.default_content()
	except TimeoutException:
		# Em alguns casos o banner não está em iframe; tenta direto no documento
		try:
			possiveis_botoes = [
				'button[aria-label="Aceitar tudo" i]',
				'button[aria-label*="Aceitar" i]',
				'button[aria-label="Accept all" i]',
				'#L2AGLb',
			]
			for sel in possiveis_botoes:
				try:
					btn = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, sel)))
					btn.click()
					break
				except TimeoutException:
					continue
		except Exception:
			pass

aceitar_consentimento_google(driver)

input = WebDriverWait(driver, 20).until(
	EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea[name="q"], input[name="q"]'))
)

input.send_keys('Montanha')
input.send_keys(Keys.RETURN)

###########################################################################
# Comando que eu falei no áudio! :)
###########################################################################
try:
	link_imagens = WebDriverWait(driver, 5).until(
		EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href*="tbm=isch"], a[aria-label="Imagens"], a[data-hveid][jsname][href*="isch"]'))
	)
	link_imagens.click()
except TimeoutException:
	# Fallback robusto: navega diretamente para a busca de imagens
	try:
		termo = input.get_attribute('value') or 'Montanha'
		driver.get(f'https://www.google.com/search?q={termo}&tbm=isch')
	except Exception:
		driver.get('https://www.google.com/search?q=Montanha&tbm=isch')

imagens = WebDriverWait(driver, 20).until(
	EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'img[jsname="Q4LuWd"], img.YQ4gaf'))
)

dados = []

for imagem in imagens:
	# Largura/altura via atributo, com fallback para naturalWidth/naturalHeight
	try:
		largura_attr = imagem.get_attribute('width')
		altura_attr = imagem.get_attribute('height')
		largura = int(largura_attr) if largura_attr else 0
		altura = int(altura_attr) if altura_attr else 0
		if largura == 0 or altura == 0:
			largura = int(driver.execute_script('return arguments[0].naturalWidth || 0;', imagem) or 0)
			altura = int(driver.execute_script('return arguments[0].naturalHeight || 0;', imagem) or 0)
	except Exception:
		largura = 0
		altura = 0

	dados.append({
		'descr': imagem.get_attribute('alt') or '',
		'largura': largura,
		'altura': altura
	})

print(f"Total de imagens coletadas: {len(dados)}")
print(dados[:5])