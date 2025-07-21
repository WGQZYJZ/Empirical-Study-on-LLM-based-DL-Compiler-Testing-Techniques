'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.roll\ntorch.roll(input, shifts, dims=None)\n'
import torch
input = torch.randn(2, 3, 5)
print(input)
output = torch.roll(input, 2, 1)
print(output)