import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 4)
transpose_data = torch.transpose(input_data, 0, 1)