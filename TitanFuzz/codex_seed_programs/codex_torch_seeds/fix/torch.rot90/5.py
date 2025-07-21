'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rot90\ntorch.rot90(input, k, dims)\n'
import torch
input = torch.randn(2, 3, 4, 5)
k = 1
dims = (2, 3)
output = torch.rot90(input, k, dims)
print(output)