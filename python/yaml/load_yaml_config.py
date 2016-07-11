from __future__ import print_function

with open('config.yml', 'r') as f:
    import yaml
    d = yaml.safe_load(f)
    
    config = d.get('config', None)
    if config:
        distro = config.get('distro', 'distro')
        print(distro)

        modules = config.get('modules', None)
        upstreams = [module for module in modules if module.has_key('upstream')]
        print(upstreams)
