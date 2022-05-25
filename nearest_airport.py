#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import click
import pandas as pd
import sys
from click.types import FloatParamType
from math import radians
from sklearn.metrics.pairwise import haversine_distances


earth_radius_meters = 6371000


class CoordinateParamType(FloatParamType):
    def __init__(self, validator_type: str):
        if validator_type not in ["latitude", "longitude"]:
            raise TypeError(
                "Invalid value for argument validator_type. Must be latitude or longitude."
            )
        super().__init__()
        self.validator_type = validator_type

    def convert(self, value, param, ctx):
        result = super().convert(value, param, ctx)
        if self.validator_type == "latitude":
            if result < -180 or result > 180:
                self.fail("Invalid latitude value. Must be between -180 and 180.")

        if self.validator_type == "longitude":
            if result < -90 or result > 90:
                raise self.fail("Invalid longitude value. Must be between -90 and 90.")

        return result


def load_csv_file(csv_file_path: str) -> pd.DataFrame:
    # we use pandas to parse the data types properly
    return pd.read_csv(csv_file_path)


@click.command()
@click.option(
    "--latitude",
    type=CoordinateParamType("latitude"),
    prompt="Latitude",
    help="Latitude",
)
@click.option(
    "--longitude",
    type=CoordinateParamType("longitude"),
    prompt="Longitude",
    help="Longitude",
)
@click.option(
    "--airport-coords-csv",
    required=False,
    type=click.Path(exists=True),
    default="uk_airport_coords.csv",
    help="Path to the csv file which holds airport " "coordinates",
)
def cli(latitude: float, longitude: float, airport_coords_csv):
    """
    Finds the nearest airport to the provided coordinate defined by --latitude and --longitude options. If these are not
    provided, then the script prompts for them.
    """
    df = load_csv_file(airport_coords_csv)
    source_lat_rad = radians(latitude)
    source_long_rad = radians(longitude)
    closest_point_distance = sys.float_info.max
    closest_point_lat = 0.0
    closest_point_long = 0.0
    closes_airport_name = ""

    # iterate rows of the csv file
    for index, row in df.iterrows():
        lat_rad = radians(row["Latitude"])
        long_rad = radians(row["Longitude"])
        # compute the Haversine distance between source and current airport's corrdinates
        result = haversine_distances(
            [[source_lat_rad, source_long_rad], [lat_rad, long_rad]]
        )

        # get the distance in kilometres
        result = result * earth_radius_meters / 1000

        if result[0][1] < closest_point_distance:
            closest_point_distance = result[0][1]
            closes_airport_name = f'{row["NAME"]} ({row["ICAO"]})'
            closest_point_lat = row["Latitude"]
            closest_point_long = row["Longitude"]

    click.echo(f"Closest airport: {closes_airport_name}")
    click.echo(f"Distance: {closest_point_distance} km")
    click.echo(f"Coordinates: {closest_point_lat} {closest_point_long}")

    return 0


if __name__ == "__main__":
    # noinspection PyArgumentList
    cli()
