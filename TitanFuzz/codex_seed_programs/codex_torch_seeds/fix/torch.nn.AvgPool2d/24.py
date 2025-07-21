'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool2d\ntorch.nn.AvgPool2d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
input = torch.randn(1, 1, 4, 4)
avgpool2d = torch.nn.AvgPool2d(2, stride=1, padding=0)
output = avgpool2d(input)
print('input: ', input)
print('output: ', output)