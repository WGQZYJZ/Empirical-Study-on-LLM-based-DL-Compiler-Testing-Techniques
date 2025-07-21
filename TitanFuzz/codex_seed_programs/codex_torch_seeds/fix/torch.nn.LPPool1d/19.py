'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LPPool1d\ntorch.nn.LPPool1d(norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
x = Variable(torch.randn(2, 3, 5))
pool = torch.nn.LPPool1d(norm_type=2, kernel_size=2, stride=2)
output = pool(x)
print('output: ', output)