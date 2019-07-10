# ScrapOverflow
An unofficial StackOverflow questions REST-API , this API allows you to search StackOverflow question-answers by providing a query string.  You can integrate this API with assistant applications like chat-bots and AI-agents to help developers search solutions easily.

## Usage :
First deploy the Flask app wherever you like.

## Endpoint information :
The endpoint for search :

```/api/search```
Parameters : 
```count : integer, Number of questions to show```
```question : string, The actual question```

## Example REST query : 

```curl -d '{"count" : 5, "question" : "What is an API ??"}' -H "Content-Type:application/json" http://localhost:9800/api/search```

Response : 
```
{"answers":[{"URL":"https://stackoverflow.com/questions/14994391/thinking-in-angularjs-if-i-have-a-jquery-background/15012542?r=SearchResults#15012542","title":"\"Thinking in AngularJS\" if I have a jQuery background?","votes":7185},{"URL":"https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python/6581949?r=SearchResults#6581949","title":"What are metaclasses in Python?","votes":6128},{"URL":"https://stackoverflow.com/questions/14220321/how-do-i-return-the-response-from-an-asynchronous-call/14220323?r=SearchResults#14220323","title":"How do I return the response from an asynchronous call?","votes":5097},{"URL":"https://stackoverflow.com/questions/630453/put-vs-post-in-rest/630475?r=SearchResults#630475","title":"PUT vs. POST in REST","votes":3791},{"URL":"https://stackoverflow.com/questions/671118/what-exactly-is-restful-programming/671132?r=SearchResults#671132","title":"What exactly is RESTful programming?","votes":2850}],"more":"https://stackoverflow.com/search?q=What+is+an+API%3F"}
```
