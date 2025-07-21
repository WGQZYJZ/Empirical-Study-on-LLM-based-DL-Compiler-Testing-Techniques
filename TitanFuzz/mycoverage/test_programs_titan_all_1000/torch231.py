import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
transpose_data = torch.t(input_data)