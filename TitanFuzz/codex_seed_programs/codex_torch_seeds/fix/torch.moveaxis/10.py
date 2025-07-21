'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.moveaxis\ntorch.moveaxis(input, source, destination)\n'
import torch
import torch
input = torch.randn(2, 3, 4)
torch.moveaxis(input, 0, 1)
print(torch.moveaxis(input, 0, 1))
print(torch.moveaxis(input, 0, (- 1)))
print(torch.moveaxis(input, (- 1), 0))
print(torch.moveaxis(input, 1, (- 1)))
print(torch.moveaxis(input, 1, 2))
print(torch.moveaxis(input, 1, 0))
print(torch.moveaxis(input, 1, 0).shape)