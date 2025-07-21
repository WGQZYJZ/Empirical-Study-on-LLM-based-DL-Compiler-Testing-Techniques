'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.moveaxis\ntorch.moveaxis(input, source, destination)\n'
import torch
input = torch.randn(2, 3, 4)
print(input)
output = torch.moveaxis(input, 2, 1)
print(output)
output = torch.moveaxis(input, 1, (- 1))
print(output)