# Guia de Uso do Pytest e Pytest-Cov

### 1. Instalando o Pytest
Instale a versão especificada do Pytest para gerenciar e executar testes em seu projeto.
```bash
pip install pytest==7.1.2
```
### 2. Rodar todos os testes
Execute todos os testes no diretório atual com saída detalhada.
```bash
pytest -v  # -v ativa o modo verbose para saída detalhada
```
### 3. Chamar um teste específico
Execute testes que correspondam a um nome específico ou padrão.
```bash
pytest -v -k cnpj  # -k filtra testes pelo nome que contém 'cnpj'
```
### 4. Chamar um teste usando Mark (decorator)
Execute testes que foram marcados com um decorador específico.
```bash
pytest -v -m metodos_veiculo  # -m filtra testes marcados com @mark.metodos_veiculo
```
### 5. Consultar os Tipos de markers
Liste todos os markers disponíveis no seu projeto de testes.
```bash
pytest --markers
```
### 6. Instalando o Pytest-Cov (cobertura de código)
Instale o plugin pytest-cov para medir a cobertura de código durante a execução dos testes.
```bash
pip install pytest-cov==3.0.0
```
### 7. Rodar todos os testes com cobertura
Execute todos os testes e meça a cobertura de código.
```bash
pytest --cov
```
### 8. Chamar um teste específico com cobertura
Execute testes específicos e meça a cobertura de código no diretório especificado.
```bash
pytest --cov=utils  # <nome do diretório>
pytest --cov=utils tests/ 
```
### 9. Especificar os termos faltantes (linhas que não têm testes)
Execute testes e reporte as linhas de código que não foram cobertas pelos testes.
```bash
pytest --cov=utils tests/ --cov-report term-missing 
```
### 10. Gerar relatório em HTML
Execute testes e gere um relatório de cobertura de código em formato HTML.
```bash
pytest --cov=utils tests/ --cov-report html
```
### 11. Gerar relatório em XML
Execute testes e gere um relatório de resultados em formato XML.
```bash
pytest --junitxml=report.xml
```
### 12. Gerar relatório de cobertura em XML
Execute testes e gere um relatório de cobertura de código em formato XML.
```bash
pytest --cov-report xml
```