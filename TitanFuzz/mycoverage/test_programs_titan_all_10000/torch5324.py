import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(2, 4, 5, 6, 7))
output = torch.nn.functional.dropout3d(input, p=0.5, training=True, inplace=False)