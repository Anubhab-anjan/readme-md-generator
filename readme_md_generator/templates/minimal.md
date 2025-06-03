# {{ name }}

{% if description %}
{{ description }}
{% endif %}

## Installation

```
{{ install if install else "npm install" }}
```

## Usage

```
{{ usage if usage else "npm start" }}
```

## Author

**{{ author }}**

* Website: {{ website }}
* GitHub: [@{{ github }}](https://github.com/{{ github }})

## License

{{ license }}

***
This README was generated with ❤️ by [readme-md-generator](https://github.com/likhonsheikhorg/readme-md-generator)
