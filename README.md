# m4atag
A command-line metadata editor for m4a files

# How to install
1. Clone the repo: `git clone https://github.com/michaelBiochemist/m4atag.git && cd m4atag`
1. Install using pip: `pip install .`
1. Invoke from the terminal: `m4atag -t "How to use m4atag" -a "Forrest Fire" tests/m4atag/runescape.m4a`

# How to run in Docker
1. Clone the repo: `git clone https://github.com/michaelBiochemist/m4atag.git && cd m4atag`
1. Build the image: `docker build -t m4atag:latest --no-cache .`
1. Run the tests: `docker run -it --rm --entrypoint pytest m4atag:latest`
1. Invoke the image from the terminal: `docker run -it --rm -v ${PWD}/tests/m4atag:/music m4atag:latest -t "How to use m4atag" -a "Forrest Fire" /music/runescape.m4a`