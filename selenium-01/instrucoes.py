# Vamos utilizar o pacote Selenium Python para manipular browsers via código:
# https://selenium-python.readthedocs.io/
#
# Para isso, ele precisa ser instalado via pip (de preferência com o VS Code fechado):
# python -m pip install selenium
#
# Depois de instalar o Selenium Python, é necessário instalar o driver referente
# ao browser que será utilizado:
#
# Chrome: https://googlechromelabs.github.io/chrome-for-testing/
# Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# Firefox: https://github.com/mozilla/geckodriver/releases
# Safari: https://webkit.org/blog/6900/webdriver-support-in-safari-10/
#
# Depois de baixar o driver, garantir que ele seja instalado/descompactado em uma
# pasta que pertença ao PATH global do sistema (de preferência com o VS Code fechado).
#
# No Linux, podem ser as pastas /usr/bin, /usr/local/bin ou outra que esteja no PATH.
# Para adicionar outra pasta ao PATH, basta editar o arquivo ~/.bashrc, e adicionar
# uma linha parecida com essa:
# export PATH=/nova/pasta/para/adicionar:${PATH}
#
# No Windows, o PATH pode ser editado clicando com o botão direito sobre o ícone do
# Computador (no Windows Explorer), depois no menu "Propriedades", em seguida "Configurações
# avançadas do sistema" e, por fim, em "Variáveis de Ambiente".