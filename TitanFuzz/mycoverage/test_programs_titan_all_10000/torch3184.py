import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 3))
output = torch.nn.functional.celu(input_data, alpha=1.0, inplace=False)