# SRI

* 1. python3 /BaseImage_dataset/obterBase.py -> (get dataset of images in csv(url, text))
* 2. python3 /images/manageBase.py           -> update database
* 3. python3 manage.py rebuild_index         -> indexing texts

# bic and bic_part are avaliable

* 4. python3 runIndexing.py                  -> indexing with LIRE
* 5. python3 runSearch.py                    -> export one query with to test (optional)

# LIRE are avaliable now 

* -text           -> ok
* -image          -> ok
* -text and image -> make tree (cerne)
