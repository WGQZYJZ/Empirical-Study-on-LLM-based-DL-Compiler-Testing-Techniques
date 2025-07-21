'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_pool2d\ntorch.nn.functional.max_pool2d(input, kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
input = torch.randn(1, 1, 4, 4)
output = torch.nn.functional.max_pool2d(input, kernel_size=2, stride=2)
print(input)
print(output)
output = torch.nn.functional.max_pool2d(input, kernel_size=2, stride=2, padding=1)
print(output)
output = torch.nn.functional.max_pool2d(input, kernel_size=2, stride=2, dilation=2)
print(output)