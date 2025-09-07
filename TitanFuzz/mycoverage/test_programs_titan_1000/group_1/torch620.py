import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, 1, 4, 4)
output_data = torch.nn.functional.hardshrink(input_data)