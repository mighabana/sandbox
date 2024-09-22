## 22/09/2024

Testing `dlt` with the spotify data, looks like an interesting data pipeline framework and pretty happy using it. You really just need to build utility functions around it to work with the data files you need and transform it into the form that `dlt` likes (ex. zip -> json -> jsonl -> dlt).

:exclamation:Still not super happy with how it automatically generates a schema based on the input to the pipeline, but I think I'm using it wrong so I may have to dig into that part a bit more

I like how it pushes you to think functionally and build out your pipeline in that way. It was how I was thinking of creating pypeline-functions and how we did it in FGI.

:bulb: The way the `dlt init` file creates it makes me think theres probably a way we can isolate each pipeline into its own image/container so that we can minimize the image size so we dont have to load the entire pypeline-functions repo for every pipeline.

Learned a lot of cool new things like reading and working with gcs files in memory instead of having to download them onto the disk and upload them as files. This could save memory especially in docker containers but obviously we'd still hit RAM limitations with large files. So this could work with smaller data but I'd still have to do it the old-fashioned process the file in batches way I was doing before at FGI with large files.

Overall I'm liking it so far and its given me a lot to think about:

1. Rearchitect my desired data pipelines framework
2. Figure out how to edit the transformations and schema generation
3. Learn how it handles multiple extracts (ex. Downloading my Spotify data multiple times) - might have to rearchitect the data seeds concept :skull:
4. Make more pipelines.