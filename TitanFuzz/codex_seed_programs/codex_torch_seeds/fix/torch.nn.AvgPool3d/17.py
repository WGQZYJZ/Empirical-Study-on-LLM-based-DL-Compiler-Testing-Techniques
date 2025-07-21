'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool3d\ntorch.nn.AvgPool3d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.Tensor(1, 1, 3, 3, 3))
input = input.fill_(2)
input[(0, 0, 1, 1, 1)] = 8
print('Input: ', input)
pool = torch.nn.AvgPool3d(kernel_size=3, stride=1, padding=0)
output = pool(input)
print('Output: ', output)