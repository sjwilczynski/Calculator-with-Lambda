# Calculator-with-Lambda

[![Build Status](https://travis-ci.org/sjwilczynski/Calculator-with-Lambda.svg?branch=master)](https://travis-ci.org/sjwilczynski/Calculator-with-Lambda)

Simple calculator app using AWS Lambda for cloud systems lab. It includes a dependency from nonstandard library (in this case numpy). The operation is passed as path parameter and the arguments are passed as query strings, for example *your_api_gateway_to_lambda/calculator/add?a=3&b=5* or *your_api_gateway_to_lambda/calculator/multiply?a=10&b=3*. In order to use the app you have to configure API Gateway using this function.

### Build fails, because I deleted my AWS account :(