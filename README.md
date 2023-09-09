# graphy
```
git clone git@github.com:dglade/graphy.git
cd graphy
docker build . -t graphy:latest
docker run -it --rm -p 5000:5000 --entrypoint /bin/bash graphy:latest
```

For now...  Inside container
```
cd /app
/gql/bin/hatch env run server
```

Visit http://localhost:5000/graphql
