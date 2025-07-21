'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.swapaxes\ntorch.swapaxes(input, axis0, axis1)\n'
import torch
a = torch.randn(3, 4, 5)
print(a)
b = torch.swapaxes(a, 1, 2)
print(b)