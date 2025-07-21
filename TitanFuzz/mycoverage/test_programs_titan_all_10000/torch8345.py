import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(10, 10))
output_data = torch.nn.functional.mish(input_data)