import yaml

""" 
config = {'database': {'host': 'localhost', 'port': 5432}}
with open('config.yml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False) """
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

print(config)