'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool2d\ntorch.nn.MaxPool2d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
input = torch.randn(20, 16, 50, 32)
maxpool = torch.nn.MaxPool2d(kernel_size=2, stride=2)
output = maxpool(input)
print(output.size())