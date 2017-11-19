# Secret Santa

1. Create a CSV file (name, email) for your participants

2. Create an HTML template file for your message

    ```
    <h1>Secret Santa</h1>
    <p>Hello {sfrom.name}</p>,
    <p>Prepare your gift for <strong>{sto.name}</strong>!
    <p>Happy Holidays!</p>
    ```

3. Create a JSON file for your email settings

    ```
    {
        "sender_name": "Secret Santa Organization",
        "sender_email": "you@gmail.com",
        "subject": "Secret Santa",
        "username": "you@gmail.com",
        "password": "app_password",
        "host": "smtp.gmail.com",
        "port": 587
    }
    ```

4. Run the script

    ```
    $ python3 -m secretsanta \
        --participants participants.csv \
        --template template.html \
        --seed 2017
        --email email_config.json
    ```


If you want to check your results, you may run the script in debug mode:

    $ python3 -m secretsanta --debug \
        --participants participants.csv \
        --seed 2017
