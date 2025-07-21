import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
result = torch.Tensor.bitwise_and(input_tensor, other=2)