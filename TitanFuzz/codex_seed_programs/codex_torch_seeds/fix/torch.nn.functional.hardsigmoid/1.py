'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardsigmoid\ntorch.nn.functional.hardsigmoid(input, inplace=False)\n'
import torch
import torch.nn.functional as F
input = torch.randn(2, 3)
print('input: ', input)
output = F.hardsigmoid(input)
print('output: ', output)
output = F.hardsigmoid(input, inplace=True)
print('output: ', output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardtanh\ntorch.nn.functional.hardtanh(input, min_val=-1, max_val=1, inplace=False)\n'
import torch
import torch.nn.functional as F
input = torch.randn(2, 3)
print('input: ', input)
output = F.hardtanh(input)
print('output: ', output)
output = F.hardtanh(input, min_val=(- 0.5), max_val=0.5, inplace=True)
print('output: ', output)