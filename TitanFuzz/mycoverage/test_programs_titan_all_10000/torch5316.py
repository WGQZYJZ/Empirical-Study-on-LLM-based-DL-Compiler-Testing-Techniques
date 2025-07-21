import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(5)
output_data = torch.expm1(input_data)