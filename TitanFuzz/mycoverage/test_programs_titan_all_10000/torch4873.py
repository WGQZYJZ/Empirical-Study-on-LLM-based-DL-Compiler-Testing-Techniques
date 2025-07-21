import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, 3)
softsign = torch.nn.Softsign()
output_data = softsign(input_data)