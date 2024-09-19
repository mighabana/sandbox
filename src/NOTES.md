Created a python script to quickly generate a pyproject.toml file through environment variables.

Initially created this experiment to create scripts to automatically setup a python project, but after coding realized that I was overengineering the solution and that it is much easier to just simply modify the text in the toml file rather than go through the hassle of managing environment variables and then programmatically generating the toml file.

I tried working with Jinja at first but realized it was much simpler to just use string interpolation with f-strings rather than mess with an entire templating engine.