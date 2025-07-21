'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool1d\ntorch.nn.AdaptiveAvgPool1d(output_size)\n'
import torch
input = torch.arange(1, 5, dtype=torch.float).view(1, 1, 4)
pool = torch.nn.AdaptiveAvgPool1d(1)
output = pool(input)
print('input: ', input)
print('output: ', output)