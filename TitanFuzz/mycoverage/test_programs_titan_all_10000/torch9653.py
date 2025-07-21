import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
other = torch.randn(3)
output_tensor = torch.Tensor.sub_(input_tensor, other)
other = torch.randn(2, 3)
output_tensor = torch.Tensor.sub_(input_tensor, other)
other = torch.randn(3, 2)
output_tensor = torch.Tensor.sub_(input_tensor, other)
other = torch.randn(2, 2)
output_tensor = torch.Tensor.sub_(input_tensor, other)
other = torch.randn(2, 3, 1)