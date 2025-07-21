'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flip\ntorch.flip(input, dims)\n'
import torch
input = torch.randn(1, 2, 3, 4)
output = torch.flip(input, [0, 2])
print(output)