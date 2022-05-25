# L3Harris Flight Data Services code challenge

An app which satisfies the requirements for the L3Harris code challenge as part of their
technical interview. A command line application which returns the closest airport to the provided coordinates.

## Getting Started

Create a virtual environment with `python -m venv venv` and install dependencies:
```bash
python -m pip install -r ./requreiements/dev.txt
```

You can also install the application system-wide:
```
pip install .
```

Run the script:
```bash
python nearest_airport.py --latitude 52.942102 --longitude -1.205220
```

Run the script (if installed globally):
```bash
nearest_airport --latitude 52.942102 --longitude -1.205220
```

### Using in a container

```bash
docker build -t nearest_airport:1 .
```
```bash
docker run -it --rm nearest_airport:1 --latitude 52.942102 --longitude -1.205220
```

## Usage

```
Usage: nearest_airport.py [OPTIONS]

  Finds the nearest airport to the provided coordinate defined by --latitude
  and --longitude options. If these are not provided, then the script prompts
  for them.

Options:
  --latitude FLOAT           Latitude
  --longitude FLOAT          Longitude
  --airport-coords-csv PATH  Path to the csv file which holds airport
                             coordinates
  --help                     Show this message and exit.

```

## Linter

Steps to run the linter:

* Run 'black .' from the top level directory. You can set your IDE up to do this on
  save: https://black.readthedocs.io/en/stable/integrations/editors.html
* Run 'flake8 .' from the top level directory. You can set your IDE up to do this on save (same method as for black).
