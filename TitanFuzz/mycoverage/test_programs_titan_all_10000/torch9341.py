import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(20, 16, 50))
pooling_L1 = torch.nn.LPPool1d(1, kernel_size=2, stride=2, ceil_mode=False)
output = pooling_L1(input_data)