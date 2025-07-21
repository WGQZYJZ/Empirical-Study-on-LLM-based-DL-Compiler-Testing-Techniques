import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.arctan(input_tensor)
input_tensor = torch.randn(4, 4)
output_tensor = torch.arctan(input_tensor)