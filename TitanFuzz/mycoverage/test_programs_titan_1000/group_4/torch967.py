import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 3))
hardswish = torch.nn.Hardswish(inplace=False)