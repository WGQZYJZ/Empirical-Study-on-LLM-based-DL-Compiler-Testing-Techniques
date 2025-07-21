'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.lp_pool1d\ntorch.nn.functional.lp_pool1d(input, norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.randn(20, 16, 50))
output = torch.nn.functional.lp_pool1d(input, 1, 2, stride=2)
print(output.size())
output = torch.nn.functional.lp_pool1d(input, 2, 2, stride=2)
print(output.size())