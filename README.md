# Twitch Channel Scrapper

A simple python scrapper to get live channles data and log it
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



## Usage

TODO: Write usage instructions
## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D
## History
TODO: Write history
## Credits
TODO: Write credits
## License
TODO: Write license