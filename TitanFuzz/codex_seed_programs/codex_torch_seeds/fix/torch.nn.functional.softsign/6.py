'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softsign\ntorch.nn.functional.softsign(input)\n'
import torch
input = torch.randn(1, 3)
print('Input data: ', input)
output = torch.nn.functional.softsign(input)
print('Output data: ', output)