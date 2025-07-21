'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LPPool1d\ntorch.nn.LPPool1d(norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
dtype = torch.FloatTensor
input_data = Variable(torch.randn(1, 3, 5).type(dtype))
print('Input data: ', input_data)
LPPool1d = torch.nn.LPPool1d(2, kernel_size=3, stride=2)
print('Output: ', LPPool1d(input_data))