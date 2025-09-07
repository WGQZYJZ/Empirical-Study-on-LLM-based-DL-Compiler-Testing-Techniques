import torch
from torch import nn
from torch.autograd import Variable

input_matrix = torch.randn(2, 3)
output_matrix = torch.sgn(input_matrix)