'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rot90\ntorch.rot90(input, k, dims)\n'
import torch
input = torch.rand(2, 3, 4)
print(input)
print(torch.rot90(input, 1, [1, 2]))
print(torch.rot90(input, 2, [1, 2]))
print(torch.rot90(input, 3, [1, 2]))
print(torch.rot90(input, 4, [1, 2]))