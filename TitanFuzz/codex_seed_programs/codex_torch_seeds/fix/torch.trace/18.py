'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.trace\ntorch.trace(input)\n'
import torch
input = torch.ones(2, 2)
print('Input:', input)
output = torch.trace(input)
print('Output:', output)