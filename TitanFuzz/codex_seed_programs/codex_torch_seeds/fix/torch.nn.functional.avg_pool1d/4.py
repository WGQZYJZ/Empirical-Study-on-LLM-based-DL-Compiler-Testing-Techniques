'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool1d\ntorch.nn.functional.avg_pool1d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'
import torch
from torch.autograd import Variable
import torch
x = torch.randn(2, 2, 4)
print(x)
y = torch.nn.functional.avg_pool1d(x, kernel_size=2, stride=1, padding=0)
print(y)