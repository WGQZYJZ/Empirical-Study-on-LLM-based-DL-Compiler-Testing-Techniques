import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(10, 10))
output = torch.nn.functional.tanhshrink(input_data)