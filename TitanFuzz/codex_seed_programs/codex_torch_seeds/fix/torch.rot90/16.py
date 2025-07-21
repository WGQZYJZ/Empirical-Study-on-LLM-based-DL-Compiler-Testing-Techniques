'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rot90\ntorch.rot90(input, k, dims)\n'
import torch
input = torch.randn(4, 3, 10, 10)
output = torch.rot90(input, 1, (2, 3))
print(output.shape)