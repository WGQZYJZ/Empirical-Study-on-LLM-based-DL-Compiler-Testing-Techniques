'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool1d\ntorch.nn.AvgPool1d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
input = Variable(torch.randn(1, 1, 4))
print(input)
avg_pool1d = nn.AvgPool1d(kernel_size=2, stride=2)
output = avg_pool1d(input)
print(output)
avg_pool1d = nn.AvgPool1d(kernel_size=2, stride=2, padding=1)
output = avg_pool1d(input)
print(output)
avg_pool1d = nn