import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(100, 100))
output = torch.nn.functional.mish(input_data)