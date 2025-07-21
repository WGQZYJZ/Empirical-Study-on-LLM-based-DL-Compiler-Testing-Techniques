'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardsigmoid\ntorch.nn.functional.hardsigmoid(input, inplace=False)\n'
import torch
input = torch.randn(3, 3)
print('Input: ', input)
output = torch.nn.functional.hardsigmoid(input)
print('Output: ', output)