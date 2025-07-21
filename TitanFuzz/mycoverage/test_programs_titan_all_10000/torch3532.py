import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(10)
output_tensor = torch.Tensor.cauchy_(input_tensor, median=1, sigma=2)