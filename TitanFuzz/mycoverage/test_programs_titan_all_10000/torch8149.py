import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, 3, 3)
output_data = torch.log1p(input_data)