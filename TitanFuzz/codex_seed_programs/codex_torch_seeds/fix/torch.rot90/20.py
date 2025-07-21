'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rot90\ntorch.rot90(input, k, dims)\n'
import torch
x = torch.randn(3, 4, 5)
print(x)
print(x.shape)
print(torch.rot90(x, 1, (1, 2)))