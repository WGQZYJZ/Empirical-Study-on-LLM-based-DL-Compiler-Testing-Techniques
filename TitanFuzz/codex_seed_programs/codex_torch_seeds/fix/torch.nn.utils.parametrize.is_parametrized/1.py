'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.parametrize.is_parametrized\ntorch.nn.utils.parametrize.is_parametrized(module, tensor_name=None)\n'
import torch
import torch.nn as nn
input = torch.randn(2, 3)
module = nn.Linear(3, 2)
print(torch.nn.utils.parameters_to_vector(module.parameters()))
print(torch.nn.utils.parametrize.is_parametrized(module))
module = nn.Linear(3, 2)
print(torch.nn.utils.parameters_to_vector(module.parameters()))
print(torch.nn.utils.parametrize.is_parametrized(module))