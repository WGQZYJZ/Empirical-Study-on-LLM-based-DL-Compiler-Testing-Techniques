'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.moveaxis\ntorch.moveaxis(input, source, destination)\n'
import torch
input = torch.randn(3, 4, 5)
print(input)
print(input.shape)
print(torch.moveaxis(input, 0, 1).shape)
print(torch.moveaxis(input, 0, 2).shape)
print(torch.moveaxis(input, 1, 2).shape)
print(torch.moveaxis(input, 2, 0).shape)
print(torch.moveaxis(input, 2, 1).shape)
print(torch.moveaxis(input, 1, 0).shape)
print(torch.moveaxis(input, 0, 0).shape)
print(torch.moveaxis(input, 1, 1).shape)
print(torch.moveaxis(input, 2, 2).shape)