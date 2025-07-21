'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool1d\ntorch.nn.AvgPool1d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'
import torch
import torch
input_data = torch.randn(1, 1, 5)
avgpool1d = torch.nn.AvgPool1d(kernel_size=3, stride=1, padding=0, ceil_mode=False, count_include_pad=True)
output = avgpool1d(input_data)
print('input_data: ', input_data)
print('output: ', output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool2d\ntorch.nn.AvgPool2d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'
import torch
import torch