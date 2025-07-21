import torch
from torch import nn
from torch.autograd import Variable
dtype = torch.FloatTensor
input_data = Variable(torch.randn(1, 3, 5).type(dtype))
LPPool1d = torch.nn.LPPool1d(2, kernel_size=3, stride=2)