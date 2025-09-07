import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 4)
output_tensor = torch.Tensor.resize_(input_tensor, 3, 2, 4)