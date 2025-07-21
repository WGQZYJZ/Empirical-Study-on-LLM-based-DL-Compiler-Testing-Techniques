'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.slogdet\ntorch.slogdet(input)\n'
import torch
input = torch.randn(2, 2)
print('Input:', input)
output = torch.slogdet(input)
print('Output:', output)