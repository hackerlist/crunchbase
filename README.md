crunchbase
==========

![Build Status](https://travis-ci.org/hackerlist/crunchbase.png)

Crunchbase Python API

Installation
------------

    $ sudo pip install crunchbase

Usage
-----

Creating an API controller:

    >>> api_key = ...
    >>> from crunchbase import Crunchbase
    >>> cb = Crunchbase(api_key)

Retrieving all members of an entity collection:

    >>> cb.companies
    >>> cb.people
    >>> cb.financial_organizations
    >>> cb.service_providers
    >>> cb.products

Performing a generic search for an entity:

    >>> cb.search('crunchbase')

Retrieving all information on a single entity:

    # "company" func may be replaced with any of the following
    # Crunchbase.ENTITIES: ['company', 'person',
    # 'financial-organization', 'product', 'service-provider']
    >>> cb.company

Retrieving posts about a single entity:

    >>> cb.posts('company', 'crunchbase', first_name='michael')
