import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
other_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.ne(input_tensor, other_tensor)
input_tensor = torch.randn(2, 3)
other_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.mul(input_tensor, other_tensor)