# Url Shortener

it's a feature that can be found in different places such as linkedin for example. where you can shorten a url
into a smaller version that redirects to the same website.

minimum requirements:

1. home page (where you can create urls)
2. an endpoint for creating a UrlInfo object that holds the original url & it's shortened version.
3. an endpoint that receives the shortened url resolves it, so you are redirected to that page.

in backend words that's:
1 Model
3 Views (1 homepage + 1 create + 1 get & get all)
3 endpoints, one for each of those views.


