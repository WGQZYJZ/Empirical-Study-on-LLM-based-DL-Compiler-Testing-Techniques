'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ParameterDict\ntorch.nn.ParameterDict(parameters=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input_data = torch.rand(10, 3)
param_dict = nn.ParameterDict(parameters={'weight': torch.rand(3, 1)})
param_dict['weight'] = torch.rand(3, 1)
param_dict.update({'bias': torch.rand(1)})
print(param_dict.keys())
print(param_dict.values())
print(param_dict.items())
print(param_dict.get('weight'))
print(param_dict.popitem())
print(param_dict)