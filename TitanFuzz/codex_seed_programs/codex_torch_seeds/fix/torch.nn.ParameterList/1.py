'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ParameterList\ntorch.nn.ParameterList(parameters=None)\n'
import torch
import torch.nn as nn
input_data = torch.randn(2, 3)
parameter_list = nn.ParameterList([nn.Parameter(torch.randn(3, 4)), nn.Parameter(torch.randn(5, 3))])
print(parameter_list)
print(parameter_list[0])
print(parameter_list[1])