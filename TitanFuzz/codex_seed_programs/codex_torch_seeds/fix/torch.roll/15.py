'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.roll\ntorch.roll(input, shifts, dims=None)\n'
import torch
input = torch.arange(12).reshape(3, 4)
print(input)
output = torch.roll(input, 1, dims=1)
print(output)