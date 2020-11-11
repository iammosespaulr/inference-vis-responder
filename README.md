# Nagoya castle or not

## 名古屋城なのか

Code for lesson 2 of Fast.ai version 3. Created ML model using Google Colaboratory. Saved all data to Google Drive.

Three classes: Nagoya castle, Osaka castle, and Kumamoto castle. Data was from Google Images. After basic cleaning, model was trained with 80~100 images of each castle.

Server is based on [cougar-or-not](https://github.com/simonw/cougar-or-not), but uses [responder](https://github.com/kennethreitz/responder) instead of [starlette](https://github.com/encode/starlette). Responder is a high-level framework, which is powered by starlette.

It's pretty sweet.

There's a Dockerfile for hosting.

## Example

![Nagoya castle](https://upload.wikimedia.org/wikipedia/commons/1/1d/080405_nagoya_csl_sakura.JPG)

```
{"predictions": [["nagoya", 0.9415864944458008], ["kumamoto", 0.057723693549633026], ["osaka", 0.0006899105501361191]]}
```
# inference-vis-responder
