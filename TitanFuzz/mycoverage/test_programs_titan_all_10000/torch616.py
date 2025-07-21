import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3, 4)
input_data_log2 = torch.Tensor.log2_(input_data)