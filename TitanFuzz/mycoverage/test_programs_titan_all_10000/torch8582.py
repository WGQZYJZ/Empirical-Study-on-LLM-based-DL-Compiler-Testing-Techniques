import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 3)
reciprocal_output = torch.Tensor.reciprocal(input_tensor)
input_tensor = torch.rand(3, 3)
round_output = torch.Tensor.round(input_tensor)
input_tensor = torch.rand(3, 3)
rsqrt_output = torch.Tensor.rsqrt(input_tensor)