# ClassicFoo

![ClassicFoo running](/running.png)

Brings the [Freitagsfoo](https://chaosdorf.de/freitagsfoo/) schedule to Classic Macs!

## Usage

### Main Program

Grab [REALBasic 5.5.3](https://www.macintoshrepository.org/39249-realbasic-5-5-3-de_de-) and obtain a license key.
After that, you can build the `ClassicFoo.rb` project file.

### Auxiliary Script

Mac OS 9 lacks support for TLS 1.2, REALBasic lacks JSON parsing capabilities. This explains the requirement for a connecting piece of software, translating [Infobeamer](https://github.com/chaosdorf/freitagsfoo-infobeamer)s JSON file into data which can be easily chewed under Mac OS 9 with REALBasic.

This piece of software is `decrypt-demystyfy.py`. It will host a HTTP server on port 8080/TCP, exposing API paths `/info` for date and moderator information, and `/talks`, exposing info about talks to be held on the current Freitagsfoo.

## License

You owe me a Mate if you use this software. For everything else, the MIT license applies.

