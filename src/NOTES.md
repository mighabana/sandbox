20/09/2024

Tried to learn how to use the Google Takeout parser to use it to ingest takeout data into my DWH.

Noticed some missing fields when playing around with the parser. Led me to contribute to the repo.. yay for my first attempt at open source contribution~

Realized its best to monkey around with new tools in jupyter notebooks it makes it much easier to wrap my head around when you can get immediate feedback.

Found a bug in orjson which I documented and raised [here](https://github.com/ijl/orjson/issues/517).

Also learned that you should change the data type of the MyActivity export to JSON instead of HTML when generating the Google Takeout.