'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool2d\ntorch.nn.MaxPool2d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
img = torch.randn(1, 1, 4, 4)
print('img = ', img)
out = torch.nn.MaxPool2d(2, 2, 0, 1, False, False)
print('out = ', out)
out = out(img)
print('out = ', out)