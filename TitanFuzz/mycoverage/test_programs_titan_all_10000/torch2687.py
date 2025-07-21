import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(1, 3, 2)
other = torch.rand(1, 3, 2)
output_tensor = torch.Tensor.add(input_tensor, other)