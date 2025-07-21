import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 1, 5))
padding = [1, 2]
output = torch.nn.ReplicationPad1d(padding)(input_data)