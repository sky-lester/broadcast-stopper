# Broadcast Stopper

This project allows you to stop a live broadcast using a REST API. It makes a POST request to the streaming server, using a user-provided `user_id` to stop the broadcast.

## Features
- Send a POST request to stop a broadcast for a given user.
- Token-based authorization for secure requests.

## Requirements

- Python 3.x
- `pyenv` and `pyenv-virtualenv` (optional, if using a virtual environment)

## Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:sky-lester/broadcast-stopper.git
    cd broadcast-stopper
    ```

2. (Optional) Set up a Python virtual environment using `pyenv` and `pyenv-virtualenv`:

    - Ensure you have `pyenv` and `pyenv-virtualenv` installed. You can follow the installation instructions [here](https://github.com/pyenv/pyenv#installation).

    - Create and activate a new virtual environment for this project:

      ```bash
      pyenv install 3.12.4  # (Replace with your desired Python version)
      pyenv virtualenv 3.12.4 broadcast_stopper_env
      pyenv local broadcast_stopper_env
      ```

    - Once activated, you'll see `(broadcast_stopper_env)` before the command prompt in your terminal.

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file by copying the example file:

    ```bash
    cp .env-example .env
    ```

5. Fill in the necessary data in the `.env` file (e.g., token and other required variables).

## Usage

To stop a broadcast for a specific `user_id`, run the script from the command line.

1. Run the script with the `user_id` as a parameter:

    ```bash
    python stop_broadcast.py <user_id>
    ```

   Replace `<user_id>` with the actual user ID of the broadcast you want to stop.

### Example

```bash
python stop_broadcast.py 12345
