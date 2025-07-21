'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.swapaxes\ntorch.swapaxes(input, axis0, axis1)\n'
import torch
x = torch.randn(2, 3, 4)
print(x)
y = torch.swapaxes(x, 0, 1)
print(y)
print(y.shape)