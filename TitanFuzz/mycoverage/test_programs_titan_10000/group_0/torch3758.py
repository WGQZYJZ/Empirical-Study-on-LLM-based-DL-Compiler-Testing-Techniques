import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(3, 3)
exponential_matrix = torch.matrix_exp(input_data)