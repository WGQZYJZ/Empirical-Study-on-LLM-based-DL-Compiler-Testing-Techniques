import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
output_data = torch.Tensor.normal_(input_data, mean=0, std=1)