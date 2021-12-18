# INSTASTAX

Instastax is a Python library to check instagram accounts stats

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install INSTASTAX.

```bash
git pull https://github.com/VertixSexyDev/instastax.git
cd instastax
pip install wheel
python3 setup.py bdist_wheel
cd dist
pip install [the wheel file]
```

## Usage

```python
import instastax

# returns amount of followers of the mentioned user
instastax.followers('example')

# returns amount of following of the mentioned user

instastax.following('example')

# returns amount of posts of the mentioned user

instastax.posts('example')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
