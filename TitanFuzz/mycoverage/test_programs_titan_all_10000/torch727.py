import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.arange(1, 13, dtype=torch.float).view(3, 4)
output_tensor = torch.Tensor.renorm(input_tensor, 1, 0, 6)