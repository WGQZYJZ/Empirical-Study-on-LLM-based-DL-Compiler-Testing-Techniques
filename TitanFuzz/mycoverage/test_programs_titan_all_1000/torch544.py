import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(10, 10))
output = torch.nn.functional.mish(input)