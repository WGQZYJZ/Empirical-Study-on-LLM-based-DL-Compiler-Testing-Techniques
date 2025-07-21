import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 10, 10)
output_data = torch.Tensor.sinc_(input_data)