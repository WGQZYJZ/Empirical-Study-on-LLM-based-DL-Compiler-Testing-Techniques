'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.lp_pool2d\ntorch.nn.functional.lp_pool2d(input, norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
import torch
input = Variable(torch.randn(1, 1, 4, 4))
output = F.lp_pool2d(input, 2, 2, 1)
print(output)