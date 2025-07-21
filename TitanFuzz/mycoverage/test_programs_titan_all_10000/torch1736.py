import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(1, 3)
output_tensor = torch.Tensor.deg2rad(input_tensor)
input_tensor = torch.rand(1, 3)
output_tensor = torch.Tensor.diag(input_tensor)
input_tensor = torch.rand(1, 3)