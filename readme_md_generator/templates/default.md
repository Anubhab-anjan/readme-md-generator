{% if use_html %}
<h1 align="center">Welcome to {{ name }} 👋</h1>
{% else %}
# Welcome to {{ name }} 👋
{% endif %}

{% if version %}
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-{{ version }}-blue.svg?cacheSeconds=2592000" />
</p>
{% endif %}

{% if description %}
> {{ description }}
{% endif %}

{% if homepage %}
### 🏠 [Homepage]({{ homepage }})
{% endif %}

{% if demo %}
### ✨ [Demo]({{ demo }})
{% endif %}

{% if docs %}
## Documentation

See [{{ docs }}]({{ docs }}) for full documentation.
{% endif %}

## Install

```sh
{{ install if install else "npm install" }}
```

## Usage

```sh
{{ usage if usage else "npm run start" }}
```

## Run tests

```sh
{{ test if test else "npm run test" }}
```

## Author

{% if author %}
👤 **{{ author }}**
{% endif %}

{% if website %}
* Website: {{ website }}
{% endif %}
{% if github %}
* GitHub: [@{{ github }}](https://github.com/{{ github }})
{% endif %}
{% if twitter %}
* Twitter: [@{{ twitter }}](https://twitter.com/{{ twitter }})
{% endif %}
{% if linkedin %}
* LinkedIn: [{{ linkedin }}](https://linkedin.com/in/{{ linkedin }})
{% endif %}

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

{% if issues %}
Feel free to check [issues page]({{ issues }}).
{% endif %}

{% if contributing %}
Check out the [contributing guide]({{ contributing }}).
{% endif %}

## Show your support

Give a ⭐️ if this project helped you!

{% if patreon %}
<a href="https://www.patreon.com/{{ patreon }}">
  <img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>
{% endif %}

{% if license %}
## 📝 License

{% if use_html %}
Copyright © {{ year }} [{{ author }}]({{ website }}).<br />
This project is [{{ license }}](LICENSE) licensed.
{% else %}
Copyright © {{ year }} [{{ author }}]({{ website }}).

This project is [{{ license }}](LICENSE) licensed.
{% endif %}
{% endif %}

***
{% if use_html %}
<div align="center">
_This README was generated with ❤️ by [readme-md-generator](https://github.com/likhonsheikhorg/readme-md-generator)_
</div>
{% else %}
_This README was generated with ❤️ by [readme-md-generator](https://github.com/likhonsheikhorg/readme-md-generator)_
{% endif %}
