'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool2d\ntorch.nn.AvgPool2d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
input = torch.randn(1, 1, 10, 10)
avg_pooling = torch.nn.AvgPool2d(kernel_size=3, stride=1, padding=1)
output = avg_pooling(input)
print('Input size:', input.size())
print('Output size:', output.size())
print('Output:', output)