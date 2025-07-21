import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, 2)
output_data = torch.special.erfinv(input_data)