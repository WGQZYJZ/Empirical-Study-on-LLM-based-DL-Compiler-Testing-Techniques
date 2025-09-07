import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(100)
output_tensor = torch.Tensor.histc(input_tensor, bins=100, min=0, max=1)