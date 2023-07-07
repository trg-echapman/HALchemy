# HALchemy

HAL-based Hypermedia API clients for humans.

> This project has lofty goals, and is in its very early stages.  Please use with caution and beware of breaking changes until at least v0.7.0

## Build steps
1. Get repository from:  
	`git clone https://github.com/trg-echapman/HALchemy.git`

2. Change into python folder:  
	`cd HALchemy\src\python`

3. Create virtual environment:  
  `python -m venv ./.venv`

4. Activate virtual environment:  
  `.\.env\Scripts\activate.ps1`

5. Install build package:  
  `pip install build`

6. Build distribution:  
  `python -m build`

## Methods
* def **url_from_rel**(resource, rel, parameters={}, template={}):
* def **post_to_url**(self, url, data):
* def **post_to_rel**(self, resource, rel, data, parameters={}, template={}):
* def **patch_resource**(self, resource, data):
* def **put_to_resource**(self, resource, data, rel='self'):
* def **get**(self, url='/'):
* def **get_from_rel**(self, resource, rel='self', parameters={}, template={}):        
* def **get_from_rel_with_lookup**(self, resource, rel, lookup, parameters={}):        
* def **delete_collection**(self, url):
* def **delete_resource**(self, resource):



## Features

* parameters and templates
* additional lookup (implicit templates)
* requests library remembers defaults
  * base url (allowing .get('/path')
  * auth (saving managing headers with each request - defaults to Basic root:password)
* can use python dict for POST/PUT/PATCH data (automatically converts to JSON)

* in post_to_url():
```python
except:
    if response.status_code == 422:
        issue = response.json().get('_issues', {}).get('name', '')
        if 'is not unique' in issue:
            new_data = json.loads(data)
            new_data['name'] += ' ~'
            return self._api.post(url, data=new_data)
    message = f'{response.status_code} {response.reason}'
    details = response.text
            raise RuntimeError(f'POST {url} - {message}\n{details}\n\n{data}')
```

## Roadmap

* chainable requests
* HAL Forms
* as many languages as we can get to
* root cache/refresh
* optimistic concurrency

## Build References
1. **PEP 518 -- Specifying Minimum Build System Requirements for Python Projects**: This is the official Python Enhancement Proposal (PEP) that introduced `pyproject.toml`. It explains why `pyproject.toml` was introduced and what problems it solves.
   https://peps.python.org/pep-0518/

2. **PEP 517 -- A build-system independent format for source trees**: This PEP proposed a standard way for Python projects to specify their build requirements and processes, enabling new tools like Poetry and Flit to emerge. It works hand-in-hand with PEP 518.
   https://peps.python.org/pep-0517/

3. **setuptools - Build System Interface**: This documentation page explains how setuptools uses the `pyproject.toml` file and gives an example of how to specify setuptools as the build system in `pyproject.toml`.
   https://setuptools.readthedocs.io/en/latest/build_meta.html

4. **How to Publish an Open-Source Python Package to PyPI**: This is a step-by-step guide that includes details on creating a `pyproject.toml` file for a setuptools-based project.
   https://realpython.com/pypi-publish-python-package/
