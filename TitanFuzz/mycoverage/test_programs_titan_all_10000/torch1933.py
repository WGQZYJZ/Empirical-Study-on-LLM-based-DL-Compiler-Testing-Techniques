import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 3)
output_tensor = torch.Tensor.erfc(input_tensor)