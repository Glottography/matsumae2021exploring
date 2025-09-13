# Releasing the dataset

## Recreate the raw data from glottography-data

In case of upstream changes in glottography-data:
```shell
cldfbench download cldfbench_matsumae2021exploring.py
```

## Recreate the CLDF data

```shell
cldfbench makecldf cldfbench_matsumae2021exploring.py --glottolog-version v5.2
cldfbench cldfreadme cldfbench_matsumae2021exploring.py
cldfbench zenodo --communities glottography cldfbench_matsumae2021exploring.py
cldfbench readme cldfbench_matsumae2021exploring.py
```

## Validation

```shell
cldf validate cldf
```

```shell
cldfbench geojson.validate cldf
```

```shell
cldfbench geojson.glottolog_distance cldf --format pipe
```

| ID | Distance | Contained | NPolys |
|:---------|-----------:|:------------|---------:|
| ainu1240 | 0.00 | True | 12 |
| chuk1273 | 0.00 | True | 10 |
| even1259 | 0.00 | True | 41 |
| even1260 | 5.14 | False | 6 |
| kala1399 | 0.00 | True | 56 |
| kore1280 | 0.00 | True | 367 |
| kory1246 | 0.00 | True | 10 |
| ngan1291 | 0.00 | True | 6 |
| nucl1643 | 0.00 | True | 404 |
| selk1253 | 0.00 | True | 6 |
| yaku1245 | 0.00 | True | 17 |
