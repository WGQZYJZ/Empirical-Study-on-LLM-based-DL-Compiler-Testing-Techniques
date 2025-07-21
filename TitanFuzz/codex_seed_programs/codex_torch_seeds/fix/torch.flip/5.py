'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flip\ntorch.flip(input, dims)\n'
import torch
input = torch.rand(2, 3, 2)
print(input)
output = torch.flip(input, [1])
print(output)
'\nTask 4: Call the API torch.flip\ntorch.flip(input, dims)\n'
output = torch.flip(input, [2])
print(output)