import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
new_empty_tensor = torch.Tensor.new_empty(input_tensor, (2, 3))