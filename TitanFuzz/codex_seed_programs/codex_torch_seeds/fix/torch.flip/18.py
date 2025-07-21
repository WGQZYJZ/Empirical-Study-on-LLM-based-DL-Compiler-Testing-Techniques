'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flip\ntorch.flip(input, dims)\n'
import torch
input = torch.randn(1, 2, 3, 4)
print(input)
print(torch.flip(input, [2]))
print(torch.flip(input, [3]))
print(torch.flip(input, [2, 3]))