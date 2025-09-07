import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, 3, 4, 4)
output_data = torch.reciprocal(input_data)