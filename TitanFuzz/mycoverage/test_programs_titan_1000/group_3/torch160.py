import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 3))
selu = torch.nn.SELU(inplace=False)
output = selu(input_data)