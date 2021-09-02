# SRI

* 1. get dataset of images in csv(url, text) and run 'python3 /BaseImage_dataset/obterBase.py'
* 2. run 'python3 /images/manageBase.py'         -> update database
* 3. run 'python3 manage.py rebuild_index'       -> indexing texts

# bic and bic_part are avaliable

* 4. 'python3 runIndexing.py'                    -> indexing with LIRE
* 5. 'python3 runSearch.py (optional)'           -> export one query with to test

# LIRE are avaliable now 

** -text           -> ok
** -image          -> ok
** -text and image -> make tree (cerne)
