'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.narrow\ntorch.narrow(input, dim, start, length)\n'
import torch
input = torch.rand(4, 4)
print(input)
output = torch.narrow(input, 0, 0, 2)
print(output)