'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool2d\ntorch.nn.AvgPool2d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 4, 4))
pool = torch.nn.AvgPool2d(kernel_size=2, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)
output = pool(input)
print('Input:\n', input)
print('\nOutput:\n', output)
print('\nOutput shape:\n', output.shape)