# Twitch Channel Scrapper

A simple python scrapper to get live channel data from Twitch and log it
into a Postgres DB.

## Installation

Make sure you have PostgresSQL installed.

First you need to get a [Client ID](https://blog.twitch.tv/client-id-required-for-kraken-api-calls-afbb8e95f843#.r2896ndiq)
from your Twitch Account to make any API calls. After you got your key,
add it to the settings.py.example file in the API Dictionary on the 
`YOUR_CLIENT_ID_HERE!!` section and delete the `.example` extension from the file. 

It should look something like this:
```
API = {
    'CLIENTID': '09r9e8g09f8b0ef8v9eer8f'
}
 ```

Then you'll need to install the python libraries required. To
do this you can run use the `requirements.txt` file:

`pip install -r requirements.txt`

You'll need to configurate the DB parameters. To do this you'll need to add the
next information to the `settings.py` file:

```
DATABASE = {
        'NAME': 'DB_NAME',
        'USER': 'USER',
        'PASSWORD': 'PASSWORD',
        'HOST': 'localhost',
    }
```

To configure the db you'll need to run the `create_tables.sql` file. To
do this you run the next command:

` psql USER -f create_tables.sql -U YOUR_DB_NAME -h localhost -W `

And that's it! You're ready to go.

## Usage

To run the script just execute the `main.py` file:
`python main.py`

### Adding API Parameter
To add your own parameters to pull from the API you just need to change
the `twitch_api_url` variable in `DataPull.py`.

### Speed VS Precision
The API response is kind of slow so it takes the script from 20-30 min
to pull all data. If you want it to go faster you can change the offset.
The bigger the offset the faster BUT it will cost Precision in terms of
the amount of data it pulls.

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## TODO List
1. Improve Performance with Mulithreading.
2. Argparser to add the parameter via terminal.
3. Pull more data.

## Credits
- Juan Pablo Flores [Github](github.com/juanpflores)
## License
TODO: Write license