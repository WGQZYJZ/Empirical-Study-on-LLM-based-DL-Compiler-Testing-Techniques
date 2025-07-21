'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.moveaxis\ntorch.moveaxis(input, source, destination)\n'
import torch
input = torch.randn(3, 4, 5)
print(input)
print(input.size())
output = torch.moveaxis(input, 0, 1)
print(output)
print(output.size())
output = torch.moveaxis(input, 1, 2)
print(output)
print(output.size())
output = torch.moveaxis(input, 0, (- 1))
print(output)
print(output.size())