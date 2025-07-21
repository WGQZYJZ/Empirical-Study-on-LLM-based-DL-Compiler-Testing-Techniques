import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 2))
output_data = torch.nn.functional.elu(input_data)