import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([[1.0, 2.0], [3.0, 4.0]])
output_tensor = torch.Tensor.mvlgamma(input_tensor, 2)