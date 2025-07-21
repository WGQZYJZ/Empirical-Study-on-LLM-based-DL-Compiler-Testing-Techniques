'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardtanh\ntorch.nn.Hardtanh(min_val=-1.0, max_val=1.0, inplace=False, min_value=None, max_value=None)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.randn(3, 4))
print('Input data: ', x)
print('Output data: ', torch.nn.Hardtanh()(x))