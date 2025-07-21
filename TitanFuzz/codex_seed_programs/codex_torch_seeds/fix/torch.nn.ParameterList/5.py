'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ParameterList\ntorch.nn.ParameterList(parameters=None)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input_data = torch.randn(3, 3)
parameters = nn.ParameterList([nn.Parameter(input_data), nn.Parameter(input_data)])
print(parameters)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Parameter\ntorch.nn.Parameter(data=None, requires_grad=True)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input_data = torch.randn(3, 3)
parameter = nn.Parameter(input_data)
print(parameter)