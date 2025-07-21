'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.numel\ntorch.numel(input)\n'
import torch
input = torch.rand(1, 3, 224, 224)
output = torch.numel(input)
print('input size:', input.size())
print('output size:', output)