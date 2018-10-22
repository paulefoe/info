import argparse
import pathlib
import os

import trafaret as T
from trafaret_config import commandline


BASE_DIR = pathlib.Path(__file__).parent.parent
DEFAULT_CONFIG_PATH = os.path.join(BASE_DIR, 'config', 'info.yaml')

TRAFARET = T.Dict({
    T.Key('postgres'):
        T.Dict({
            'database': T.String(),
            'user': T.String(),
            'password': T.String(),
            'host': T.String(),
            'port': T.Int(),
        }),
})


def get_config(argv=None) -> dict:
    ap = argparse.ArgumentParser()
    commandline.standard_argparse_options(
        ap,
        default_config=DEFAULT_CONFIG_PATH
    )
    # ignore unknown options
    options, unknown = ap.parse_known_args(argv)

    config = commandline.config_from_options(options, TRAFARET)
    return config
