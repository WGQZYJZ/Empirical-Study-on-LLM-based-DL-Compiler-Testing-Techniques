'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LPPool1d\ntorch.nn.LPPool1d(norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch
from torch.autograd import Variable
import torch.nn as nn
input_data = Variable(torch.randn(1, 1, 3))
print(input_data)
pool1d = nn.LPPool1d(norm_type=2, kernel_size=3, stride=1, ceil_mode=True)
output = pool1d(input_data)
print(output)