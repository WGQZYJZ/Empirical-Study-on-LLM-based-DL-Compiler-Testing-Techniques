'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.parametrize.is_parametrized\ntorch.nn.utils.parametrize.is_parametrized(module, tensor_name=None)\n'
import torch
input_data = torch.randn(5, 5)
is_parametrized = torch.nn.utils.parametrize.is_parametrized(input_data)
print(is_parametrized)