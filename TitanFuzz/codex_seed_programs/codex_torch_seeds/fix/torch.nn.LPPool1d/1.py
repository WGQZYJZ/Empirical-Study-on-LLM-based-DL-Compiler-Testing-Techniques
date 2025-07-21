'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LPPool1d\ntorch.nn.LPPool1d(norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 3, 5))
pooling = torch.nn.LPPool1d(1, 3, stride=2)
output = pooling(input)
print(output)