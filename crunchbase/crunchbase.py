#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
    crunchbase
    ~~~~~~~~~~
    Crunchbase unofficial API

    :copyright: (c) 2014 by Hackerlist, Inc
    :license: see LICENSE
"""

import requests
import argparse
from functools import partial

class Crunchbase(object):

    API_BASE_URL = 'http://api.crunchbase.com'
    ENTITIES = ['company', 'person', 'financial-organization',
                'product', 'service-provider']
                     
    def __init__(self, api_key='', api_version=1):
        self.api_key = api_key
        self.version = api_version
        self._setup()

    def _setup(self):
        """Dynamically compose GET partials for each entity"""
        for e in self.ENTITIES:
            setattr(self, e.replace('-', '_'), partial(self.get, e))

    def uri(self, entity=None, name=None):
        if entity not in self.ENTITIES:
            entity = 'search'
        endpoint = '%s/%s' % (entity, name) if name else entity
        return "%s/v/%s/%s.js" % (self.API_BASE_URL, self.version, endpoint)

    def get(self, entity=None, name=None, **data):
        """Performs a GET HTTP request to crunchbase for a resource.
        
        params:
            entity - a member of Crunchbase.ENTITIES
            name - the

        If no entity or name are provided, endpoint falls back to
        search API.
        """
        data.update({'api_key': self.api_key})
        url = self.uri(entity=entity, name=name)
        r = requests.get(url, data=data)
        try:
            return r.json()
        except ValueError:
            raise ValueError(r.content)

    def posts(self, entity, name, first_name='', last_name=''):
        """Retrieves posts about entity by first and last name"""
        data = {'first_name': first_name,
                'last_name': last_name
                }
        return self.cb.get(self.entity, name, **data)

    @property
    def companies():
        return self.get('companies')

    @property
    def people():
        return self.get('people')

    @property
    def financial_organizations(self):
        return self.get('financial-organizations')

    @property
    def service_providers():
        return self.get('service-providers')

    @property
    def products():
        return self.get('products')

    @property
    def search(self, query):
        return self.get(query=query)

def argparser():
    parser = argparse.ArgumentParser(description="Crunchbase Python API")
    parser.add_argument("-t", "--token", type=str, default='',
                        help="Crunchbase api_key")
    parser.add_argument("-e", "--entity", type=str, default='',
                        help="Entity type (company, person, etc.)")
    parser.add_argument("-n", "--name", type=str, default='',
                        help="Entity name (crunchbase, google)")
    return parser

if __name__ == "__main__":
    parser = argparser()
    args = parser.parse_args()

    if not (args.entity or args.name):
        raise AttributeError("Entity type -e and name -n required")

    if not args.token:
        raise AttributeError("Crunchbase API Token required: -t ")
    cb = Crunchbase(args.token)
    print cb.get(args.entity, args.name)
