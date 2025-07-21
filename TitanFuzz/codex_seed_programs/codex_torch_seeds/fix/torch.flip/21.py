'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flip\ntorch.flip(input, dims)\n'
import torch
x = torch.randn(1, 2, 3, 4)
print(x)
flipped_x = torch.flip(x, dims=[2])
print(flipped_x)