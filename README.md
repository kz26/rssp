# rssp

A simple proxy server for RSS/Atom feeds, built with Pyramid. Useful if a site has blocked your newsfeed client from accessing its feeds. (*cough* Reddit *cough*)

## Requirements

* Python 3.x

## Usage

```
pip install -r requirements.txt
python setup.py develop 
pserve production.ini
```

Proxy a feed via `/feed/FEED_URL`

## License

MIT
