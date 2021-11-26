# Dynamic certificate parser

The online certificate parser utility that can parse certificate data for the public domains.

## General instructions

Pass a public accessible domain using the `domain` parameter to the URL (https://somethingwentwrong.herokuapp.com).

> Example: https://somethingwentwrong.herokuapp.com?domain=google.com

## Build and deploy instructions

The steps to reproduce the online application for local use can be deduced from
[workflow.yml](.github/workflows/workflow.yml) and the muti-staged [Dockerfile](./Dockerfile).

## Build logs

Build and release pipeline for the https://somethingwentwrong.herokuapp.com can be
found here: [link](https://github.com/Biswajee/dynamic-certigo/actions/workflows/workflow.yml)
