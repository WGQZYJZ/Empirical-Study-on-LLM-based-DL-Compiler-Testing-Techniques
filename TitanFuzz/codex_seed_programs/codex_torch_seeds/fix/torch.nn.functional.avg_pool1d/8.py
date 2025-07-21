'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool1d\ntorch.nn.functional.avg_pool1d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'
import torch
import torch.nn.functional as F
x = torch.randn(1, 3, 5)
print('Input: ', x)
y = F.avg_pool1d(x, kernel_size=3, stride=1, padding=0)
print('Output: ', y)