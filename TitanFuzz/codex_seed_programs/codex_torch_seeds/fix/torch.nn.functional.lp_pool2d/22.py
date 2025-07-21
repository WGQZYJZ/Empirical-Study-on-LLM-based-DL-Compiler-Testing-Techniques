'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.lp_pool2d\ntorch.nn.functional.lp_pool2d(input, norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
import torch
input = Variable(torch.randn(1, 3, 5, 5))
output = F.lp_pool2d(input, norm_type=2, kernel_size=3, stride=2)
print(output)
output = F.lp_pool2d(input, norm_type=2, kernel_size=3, stride=2, ceil_mode=True)
print(output)