import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.arange(1, 6)
output_tensor = torch.Tensor.multiply_(input_tensor, 2)