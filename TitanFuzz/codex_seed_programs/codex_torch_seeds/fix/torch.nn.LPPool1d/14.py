'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LPPool1d\ntorch.nn.LPPool1d(norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
dtype = torch.FloatTensor
input_data = Variable(torch.randn(1, 1, 4).type(dtype))
pool = torch.nn.LPPool1d(norm_type=1, kernel_size=2, stride=2)
print('input: ', input_data)
print('output: ', pool(input_data))