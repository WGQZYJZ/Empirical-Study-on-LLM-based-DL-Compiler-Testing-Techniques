'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ParameterList\ntorch.nn.ParameterList(parameters=None)\n'
import torch
input_data = [torch.rand(1, 2), torch.rand(3, 4)]
param_list = torch.nn.ParameterList(input_data)
print('param_list = ', param_list)