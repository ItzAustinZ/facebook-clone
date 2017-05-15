# facebook-clone
A very simple clone of Facebook written to get more practice with web development. Uses Python Flask as the backend.

## How to run
### With Docker
This is the easiest way to make sure that it will work. Make sure you have
Docker installed on your machine.

Build the container. From the source directory, run this command:

```
docker build -t facebook-clone .
```

The server will run on the container's port 80. When running the container,
make sure to map whatever port you want to see the website on to port 80.
For example, to see the website on port 5000, run this command:

```
docker run --rm -p 5000:80 facebook-clone
```

And then visit [http://localhost:5000](http://localhost:5000).