'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.moveaxis\ntorch.moveaxis(input, source, destination)\n'
import torch
input = torch.randn(4, 3, 5)
print('Input:', input)
output = torch.moveaxis(input, 0, 1)
print('Output:', output)