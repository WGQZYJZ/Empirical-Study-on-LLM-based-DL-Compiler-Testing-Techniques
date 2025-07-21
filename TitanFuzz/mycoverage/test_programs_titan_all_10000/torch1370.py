import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 3, 224, 224))
output = torch.nn.Hardswish(inplace=False)(input_data)