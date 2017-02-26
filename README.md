# TensorFlow Deps Offline Fetcher

This is a fetcher for TensorFlow dependences for offline installation from source. This is a very early version and only TensorBoard dependences can be fetched automatically. TensorFlow dependences fetcher will be supported in the future.

What's more, only TensorFlow 1.0 has been tested.

## Usage

1. Set `tfboard_deps_path` in `tfboard_fetcher.py`.
2. Copy `WORKSPACE` file from TensorFlow to where `tfboard_fetcher.py` is.
3. Run `tfboard_fetcher.py`.
