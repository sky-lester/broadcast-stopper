# Broadcast Stopper

This project allows you to stop a live broadcast using a REST API. It makes a POST request to the streaming server, using a user-provided `user_id` to stop the broadcast.

## Features
- Send a POST request to stop a broadcast for a given user.
- Token-based authorization for secure requests.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/broadcast-stopper.git
    cd broadcast-stopper
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file by copying the example file:

    ```bash
    cp .env.example .env
    ```

4. Fill in the necessary data in the `.env` file (e.g., token and other required variables).

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
