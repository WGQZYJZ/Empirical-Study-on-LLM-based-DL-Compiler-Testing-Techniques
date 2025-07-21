'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardsigmoid\ntorch.nn.functional.hardsigmoid(input, inplace=False)\n'
import torch
x = torch.randn(5, 5)
print('Input data: ', x)
y = torch.nn.functional.hardsigmoid(x)
print('Output data: ', y)