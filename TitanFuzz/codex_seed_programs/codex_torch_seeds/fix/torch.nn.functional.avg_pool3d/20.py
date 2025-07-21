'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool3d\ntorch.nn.functional.avg_pool3d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
import torch
input = torch.randn(1, 1, 4, 4, 4)
avg_pool3d = torch.nn.functional.avg_pool3d(input, kernel_size=(2, 2, 2))
print('input: ', input)
print('avg_pool3d: ', avg_pool3d)