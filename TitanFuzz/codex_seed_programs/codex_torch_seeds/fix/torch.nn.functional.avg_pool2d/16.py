'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool2d\ntorch.nn.functional.avg_pool2d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
input = torch.randn(20, 16, 50, 32)
output = torch.nn.functional.avg_pool2d(input, kernel_size=5, stride=1, padding=2)
print(output.size())