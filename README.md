# SRI (Sistema de Recuperação de Imagens)

#### Get dataset of images in csv(url, text)
```jsx 
python3 /BaseImage_dataset/obterBase.py
```
#### Update database
```jsx 
python3 /images/manageBase.py
```
#### Indexing texts
```jsx 
python3 manage.py rebuild_index
```

#### Indexing with LIRE (bic and bic_part are avaliable)
```jsx 
python3 runIndexing.py
```
#### Export one query with to test (optional)
```jsx 
python3 runSearch.py
```
