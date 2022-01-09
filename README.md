### report
* If I want to be honest, this was my first data-oriented project on Fastapi. For projects like this, I prefer to use frameworks that contain built-in ORM. I spent most of my time learning about Fastapi (yes, I know you are in love with it! )
* To find a better layout, I saw a few sample projects template and project generators (ex Fastapi project generator ), but unfortunately, they have a poor structure for their project. (i can't understand why they pass DB object in view! as a param ) so I tried to create MVC based pattern. I separated view, controller, and model to handle dependency injection in every module separately. I also made a Core package to manage settings, DB, and WSGI. I'm not too fond of the .env pattern. So you could add your local setting in src/core/settings/local.py. This file is ignored and only exists on your computer.
* To launch project locally, type make docker.
* As you wanted, I did items 1 and 2. There is an auto-generated OpenApi file, but it should be better.
* http://127.0.0.1:8080/items/ return list of all records received from remote API. You could change the response with skip and limit. Also, you could filter by year. This is the only filter I added (i need time for other tasks). 
* if you call http://127.0.0.1:8080/items/{item_id} you will find a parameter in response called chart_id. that contains a random uuid4. use this id in http://127.0.0.1:8080/charts/{chart_id}. this return plotly chart like you wanted. I could save this data on a model. But it did not seem necessary. every chart will be created in the background, and the files will be saved in src/charts path 
* there is not any test or diagram (I'm so sorry) because all my time was up, and I needed more time 
* if I had more time:
  - the logger is ugly. I change it
  - i add more tests
  - i rewrite openapi file
