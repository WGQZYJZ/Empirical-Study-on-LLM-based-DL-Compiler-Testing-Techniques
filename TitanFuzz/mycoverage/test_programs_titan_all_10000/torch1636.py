import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
expand_tensor = torch.Tensor.expand(input_tensor, 3)
expand_tensor = torch.Tensor.expand(input_tensor, 2, 3)