##Autotests for effective-mobile
###Instalation
```
git clone https://github.com/Moonlin14/effective_mobile.git

```
pip install -r requirements.txt
```
##Local tests run
```
pytest -v -s --alluredir allure-results
```

```
allure serve allure-results
```
##Docker tests run
```
docker build -t {image name} .
```

```
docker run --rm {image name}
```