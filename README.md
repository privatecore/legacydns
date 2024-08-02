# legacydns for Python

You can use `visibleip.com` as your IPv4 translator. It is run by IPv6 enthusiasts and is anycasted across 16 different locations. It's nothing special — just running legacy DNS, which helps create domain names for IP addresses when using IPv6 + NAT64 + DNS64.

## Features

- Responds with the A record corresponding a name, like `1.1.1.1.visibleip.com` will return `1.1.1.1`

## Example

- Try it out, type `host IPv4_ADDRESS.visibleip.com` in your terminal.

## Use Case

- This makes it easier to work with your grandpa's legacy IPv4 networks.

## Usage

- Navigate to the project directory: `cd /path/to/legacydns`
- Build the Docker image: `docker compose build`
- Run the Docker Compose setup: `docker compose up`

You'll need to setup a Nameserver and DNS prior, of course.

## License

Distributed under the COOL License.

Copyright (c) 2024 IPv6.rs <https://ipv6.rs>
All Rights Reserved
