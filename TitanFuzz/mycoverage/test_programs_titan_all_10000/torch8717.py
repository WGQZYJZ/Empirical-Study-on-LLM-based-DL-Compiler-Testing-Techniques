import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 4, 5)
output_tensor = torch.Tensor.resize_(input_tensor, 3, 5)