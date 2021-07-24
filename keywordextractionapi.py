
import requests

url = "https://textanalysis-keyword-extraction-v1.p.rapidapi.com/keyword-extractor-text"

payload = "text=Keyword%20extraction%20is%20tasked%20with%20the%20automatic%20identification%20of%20terms%20that%20best%20describe%20the%20subject%20of%20a%20document.%20Key%20phrases%2C%20key%20terms%2C%20key%20segments%20or%20just%20keywords%20are%20the%20terminology%20which%20is%20used%20for%20defining%20the%20terms%20that%20represent%20the%20most%20relevant%20information%20contained%20in%20the%20document.%20Although%20the%20terminology%20is%20different%2C%20function%20is%20the%20same%3A%20characterization%20of%20the%20topic%20discussed%20in%20a%20document.%20Keyword%20extraction%20task%20is%20important%20problem%20in%20Text%20Mining%2C%20Information%20Retrieval%20and%20Natural%20Language%20Processing.%20Keyword%20assignment%20vs.%20extraction%20Keyword%20assignment%20methods%20can%20be%20roughly%20divided%20into%3A%20keyword%20assignment%20(keywords%20are%20chosen%20from%20controlled%20vocabulary%20or%20taxonomy)%20and%20keyword%20extraction%20(keywords%20are%20chosen%20from%20words%20that%20are%20explicitly%20mentioned%20in%20original%20text).%20Methods%20for%20automatic%20keyword%20extraction%20can%20be%3A%20supervised%2C%20semi-supervised%20and%20unsupervised.%20Unsupervised%20methods%20can%20be%20further%20divided%20into%3A%20simple%20statistics%2C%20linguistics%2C%20graph-based%20and%20other%20methods.&wordnum=5"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-key': "609c196889msh54ed4c8d249216ap14f165jsn7cb079b6f71d",
    'x-rapidapi-host': "textanalysis-keyword-extraction-v1.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)