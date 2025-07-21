import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(5, 3)
output_data = torch.frac(input_data)