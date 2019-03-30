# WeirdText encoder and decoder - Django REST API

Django REST app exposing two endpoints to encode text (any) or decode text (in the encoder
format).


## Deployment

#### With runserver
1) Create a virtual environment and activate it. For Python3:
    ```
    $ python3 -m venv $PATH_TO_VENV
    $ source $PATH_TO_VENV/bin/activate
    ```

2) Install modules:
    ```
    $ pip3 install -r requirements.txt
    ```

3) Runserver:
    ```
    $ python manage.py runserver
    ```

The app is running at http://127.0.0.1:8000.

#### With Docker
1) Run the bash script (may require `sudo` permissions):
    ```
    $ ./build_and_run.sh
    ```

The app is running at http://127.0.0.1:8000.


## API

There are two endpoints available:
* **/v1/encode**

    **Method:** POST
    
    **Data (body) Params:** text=Text to encode!
    
    **Success Response:**
    
     Code: 200
     
     Content: "Encoded text"
     
    **Error Response:**
    
    Generated when request does not have the 'text' key in the body.
    
    Code: 400
    
    Content: "Some error message"
        
    **Sample Call:**
    
        $ curl --data 'text=For example... this text' -X POST http://localhost:8000/v1/encode
        
    Output (example): `"\n-weird-\nFor epxlame... tihs txet\n-weird-\nexample text this"`
        
* **/v1/decode**

    **Method:** POST
    
    **Data (body) Params:** text=Encoded text in the WeirdText encoder format
    
    **Success Response:**
    
     Code: 200
     
     Content: "Decoded text"
     
    **Error Response:**
    
    Generated when request does not have the 'text' key in the body.
    
    Code: 400
    
    Content: "Some error message"
        
    **Sample Call:**
    
        $ curl --data 'text=\n-weird-\nFor elpxame... tihs txet\n-weird-\nexample text this' -X POST http://localhost:8000/v1/decode
        
    Output: `"For example... this text"`
    
## Tests

Command to run tests:

```
$ python manage.py test
```