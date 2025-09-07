import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 5))
output = torch.nn.functional.softsign(input_data)
input_data = Variable(torch.randn(5, 5))
output = torch.nn.functional.softshrink(input_data)