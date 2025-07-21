'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool2d\ntorch.nn.functional.avg_pool2d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
import torch
input = torch.rand(1, 1, 3, 3)
print('input: \n', input)
output = torch.nn.functional.avg_pool2d(input, kernel_size=3, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)
print('output: \n', output)