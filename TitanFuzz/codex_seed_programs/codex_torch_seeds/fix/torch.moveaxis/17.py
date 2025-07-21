'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.moveaxis\ntorch.moveaxis(input, source, destination)\n'
import torch
input = torch.rand(2, 3, 4)
print(input)
print(torch.moveaxis(input, 0, 1))
print(torch.moveaxis(input, 1, 2))
print(torch.moveaxis(input, 2, 0))
print(torch.transpose(input, 0, 1))
print(torch.transpose(input, 1, 2))
print(torch.transpose(input, 2, 0))