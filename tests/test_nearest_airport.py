# -*- coding: utf-8 -*-
import pytest
from nearest_airport import cli


@pytest.mark.parametrize(
    "latitude,longitude,expected_airport_name",
    [
        (52.942102, -1.205220, "NOTTINGHAM"),
        (52.681517, -2.422482, "SHAWBURY"),
        (53.926093, -1.225241, "CHURCH FENTON"),
    ],
)
def test_returns_correct_closest_airport(
    latitude, longitude, expected_airport_name, cli_runner
):
    result = cli_runner.invoke(cli, ["--latitude", latitude, "--longitude", longitude])

    assert result.exit_code == 0
    assert expected_airport_name in result.output


@pytest.mark.parametrize(
    "latitude,longitude,expected_wrong_option",
    [
        ("invalid_test_value1", -1.205220, "latitude"),
        (53.926093, "invalid_test_value1", "longitude"),
    ],
)
def test_validates_coordinate_option_type_properly(
    latitude, longitude, expected_wrong_option, cli_runner
):
    result = cli_runner.invoke(cli, ["--latitude", latitude, "--longitude", longitude])

    expected_error_message = (
        f"Error: Invalid value for '--{expected_wrong_option}': "
        f"'{latitude if expected_wrong_option == 'latitude' else longitude}' is not a valid float."
    )

    assert result.exit_code == 2
    # last line contains the error message
    assert result.output.splitlines()[-1] == expected_error_message


@pytest.mark.parametrize(
    "latitude,longitude,expected_wrong_option",
    [(189.55, -1.52, "latitude"), (51.44, -92, "longitude")],
)
def test_validates_coordinate_option_range_properly(
    latitude, longitude, expected_wrong_option, cli_runner
):
    result = cli_runner.invoke(cli, ["--latitude", latitude, "--longitude", longitude])

    expected_error_message = (
        f"Error: Invalid value for '--{expected_wrong_option}': "
        f"Invalid {expected_wrong_option} value. Must be between "
        f"{-180 if expected_wrong_option == 'latitude' else -90} and "
        f"{180 if expected_wrong_option == 'latitude' else 90}."
    )

    assert result.exit_code == 2
    # last line contains the error message
    assert result.output.splitlines()[-1] == expected_error_message
