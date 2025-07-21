'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool1d\ntorch.nn.AvgPool1d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'
import torch
import torch
input = torch.randn(2, 3, 5)
output = torch.nn.AvgPool1d(kernel_size=3, stride=1, padding=0)(input)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool2d\ntorch.nn.AvgPool2d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'
import torch
import torch
input = torch.randn(2, 3, 5, 5)
output = torch.nn.AvgPool2d(kernel_size=3, stride=1, padding=0)(input)