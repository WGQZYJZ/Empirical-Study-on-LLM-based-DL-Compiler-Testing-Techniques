import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 5, 5)
output_data = torch.Tensor.sinc(input_data)