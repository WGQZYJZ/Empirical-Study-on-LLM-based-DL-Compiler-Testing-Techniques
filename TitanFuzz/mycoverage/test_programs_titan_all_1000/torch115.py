import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(10, 10)
output_tensor = torch.Tensor.bernoulli_(input_tensor, p=0.5)