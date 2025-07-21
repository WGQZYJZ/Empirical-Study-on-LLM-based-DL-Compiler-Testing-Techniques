'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.parametrize.is_parametrized\ntorch.nn.utils.parametrize.is_parametrized(module, tensor_name=None)\n'
import torch
module = torch.nn.Linear(2, 3)
tensor_name = 'weight'
is_parametrized = torch.nn.utils.parametrize.is_parametrized(module, tensor_name)
print(is_parametrized)