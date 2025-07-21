'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ELU\ntorch.nn.ELU(alpha=1.0, inplace=False)\n'
import torch
import torch.nn as nn
input = torch.randn(2, 3)
print('input: \n', input)
elu = nn.ELU(alpha=1.0, inplace=False)
output = elu(input)
print('output: \n', output)