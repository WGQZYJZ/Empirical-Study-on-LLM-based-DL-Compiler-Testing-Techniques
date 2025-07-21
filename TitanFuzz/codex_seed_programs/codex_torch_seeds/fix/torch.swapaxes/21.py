'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.swapaxes\ntorch.swapaxes(input, axis0, axis1)\n'
import torch
x = torch.arange(0, 9, 1)
x = x.view(3, 3)
print(x)
y = torch.swapaxes(x, 0, 1)
print(y)