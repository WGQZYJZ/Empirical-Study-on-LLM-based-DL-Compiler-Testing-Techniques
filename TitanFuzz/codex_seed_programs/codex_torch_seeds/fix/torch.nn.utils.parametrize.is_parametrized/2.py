'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.parametrize.is_parametrized\ntorch.nn.utils.parametrize.is_parametrized(module, tensor_name=None)\n'
import torch
import torch.nn as nn
import torch.nn.utils.parametrize as parametrize
input_data = torch.randn(1, 10, requires_grad=True)
module = nn.Linear(10, 10)
tensor_name = 'weight'
is_parametrized = parametrize.is_parametrized(module, tensor_name)
print(is_parametrized)