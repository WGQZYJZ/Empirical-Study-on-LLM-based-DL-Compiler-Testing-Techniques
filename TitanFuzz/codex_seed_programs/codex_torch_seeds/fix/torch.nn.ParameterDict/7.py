'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ParameterDict\ntorch.nn.ParameterDict(parameters=None)\n'
import torch
import torch.nn as nn
param_dict = nn.ParameterDict(parameters=None)
param_dict['weight_1'] = nn.Parameter(torch.randn(2, 3))
param_dict['weight_2'] = nn.Parameter(torch.randn(3, 2))
param_dict['weight_3'] = nn.Parameter(torch.randn(2, 3))