'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool2d\ntorch.nn.functional.avg_pool2d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
import torch
input = torch.tensor([[[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]]])
output = torch.nn.functional.avg_pool2d(input, kernel_size=2, stride=2)
print(output)
'\nExpected output:\ntensor([[[[  4.5000,   6.5000,   8.5000],\n          [ 12.5000,  14.5000,  16.5000],\n          [ 20.5000,  22.5000,  24.5000]]]])\n'