import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 4)
output_tensor = torch.Tensor.mvlgamma_(input_tensor, 2)