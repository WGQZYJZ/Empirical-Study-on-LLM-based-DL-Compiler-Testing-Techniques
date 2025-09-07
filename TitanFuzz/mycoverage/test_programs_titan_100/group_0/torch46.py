import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
other = torch.randn(3, 3)
output_tensor = torch.Tensor.greater_equal_(input_tensor, other)
input_tensor = torch.randn(3, 3)
index = torch.tensor([0, 2])
dim = 0
output_tensor = torch.Tensor.index_select(input_tensor, dim, index)
input_tensor = torch.randn