import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(3)
output_data = torch.Tensor.mvlgamma(input_data, 3)