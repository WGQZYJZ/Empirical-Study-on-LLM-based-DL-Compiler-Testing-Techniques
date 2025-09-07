import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
size = (2, 3)
output_tensor = torch.Tensor.new_zeros(input_tensor, size)