import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3)
output_data = torch.log1p(input_data)
output_data = torch.log1p_(input_data)