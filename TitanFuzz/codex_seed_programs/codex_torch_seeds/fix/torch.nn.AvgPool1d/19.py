'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool1d\ntorch.nn.AvgPool1d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'
import torch
data = torch.arange(0, 16).view(1, 1, 16)
pooling = torch.nn.AvgPool1d(kernel_size=3, stride=2, padding=0, ceil_mode=False, count_include_pad=True)
output = pooling(data)
print('The input data is: \n', data)
print('The output is: \n', output)