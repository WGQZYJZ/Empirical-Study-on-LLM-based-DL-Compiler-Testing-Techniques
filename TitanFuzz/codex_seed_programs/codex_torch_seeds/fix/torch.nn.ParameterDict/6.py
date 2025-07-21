'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ParameterDict\ntorch.nn.ParameterDict(parameters=None)\n'
import torch
data = {'name1': torch.randn(3), 'name2': torch.randn(3), 'name3': torch.randn(3)}
parameter_dict = torch.nn.ParameterDict(data)
print('parameter_dict: {}'.format(parameter_dict))
print('parameter_dict.items(): {}'.format(parameter_dict.items()))
print('parameter_dict.keys(): {}'.format(parameter_dict.keys()))
print('parameter_dict.values(): {}'.format(parameter_dict.values()))
print("\nparameter_dict['name1']: {}".format(parameter_dict['name1']))
print("parameter_dict['name2']: {}".format(parameter_dict['name2']))
print("parameter_dict['name3']: {}".format(parameter_dict['name3']))
print