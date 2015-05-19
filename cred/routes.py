"""
A quick overview of the routes can be seen in the table below. An API key with
read permission has access to all GET requests. Write permission gives access
to all GETs and POSTs in the table below. Finally, the admin permission gives
access to a special endpoint that can create API keys.

| Resource                        | Method |
|---------------------------------|--------|
| /auth                           | GET    |
| /events                         | GET    |
| /events/<int>                   | GET    |
| /clients                        | GET    |
| /clients/me                     | GET    |
| /clients/<int>                  | GET    |
| /clients/<int>/events           | GET    |
| /clients/<int>/events           | POST   |
| /clients/<int>/subscribedevents | GET    |

Additionally the following query parameters can also be appended to the
resource, for extra fine-tuning. The parameters below work when using GET
requests on the following resources: /events, /clients, /clients/<int>/events
and /clients/<int>/subscribedevents.

| Parameter    | Function                                           |
|--------------|----------------------------------------------------|
| full=<bool>  | Return the full information instead of just IDs    |
| before=<int> | Returns IDs lower than <int>                       |
| after=<int>  | Returns IDs higher than <int>                      |
| limit=<int>  | Limit the number of items to <int> items           |
| offset=<int> | Skip <int> number of items before fetching         |

This will form the basis of the API, from which many actions can be performed.

Earlier, admin permissions were mentioned. The route that they give access to
is,

| Resource                        | Method |
|---------------------------------|--------|
| /apikeys                        | GET    |
| /apikeys                        | POST   |
| /apikeys/<int>                  | GET    |

Where the GET requests also accept the parameters mentioned earlier.

"""
from cred import api
from cred.resources.auth import Auth
from cred.resources.apikeys import *
from cred.resources.events import *
from cred.resources.clients import *
from cred.resources.clients_events import *


# Generate API keys and read (requires admin permissions)
api.add_resource(
    APIKeys,
    '/apikeys',
    endpoint='apikeys'
)
api.add_resource(
    APIKeysItem,
    '/apikeys/<int:apikey_id>',
    endpoint='apikeys_item'
)

# Authentication of clients
api.add_resource(
    Auth,
    '/auth',
    endpoint='auth'
)

# Access to all events
api.add_resource(
    Events,
    '/events',
    endpoint='events'
)
api.add_resource(
    EventsItem,
    '/events/<int:event_id>',
    endpoint='events_item'
)

# Client related information
api.add_resource(
    Clients,
    '/clients',
    endpoint='clients'
)
api.add_resource(
    ClientsMe,
    '/clients/me',
    endpoint='clients_me'
)
api.add_resource(
    ClientsItem,
    '/clients/<int:client_id>',
    endpoint='clients_item'
)

# Events pertaining to a specific client
api.add_resource(
    ClientsEvents,
    '/clients/<int:client_id>/events',
    endpoint='clients_events'
)
api.add_resource(
    ClientsSubscribedEvents,
    '/clients/<int:client_id>/subscribedevents',
    endpoint='clients_subscribedevents'
)
