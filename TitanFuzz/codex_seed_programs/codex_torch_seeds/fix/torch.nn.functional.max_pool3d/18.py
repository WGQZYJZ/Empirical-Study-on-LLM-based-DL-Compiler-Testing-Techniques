'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_pool3d\ntorch.nn.functional.max_pool3d(input, kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 3, 3, 3))
output = torch.nn.functional.max_pool3d(input, kernel_size=3, stride=2, padding=0)
print(output)