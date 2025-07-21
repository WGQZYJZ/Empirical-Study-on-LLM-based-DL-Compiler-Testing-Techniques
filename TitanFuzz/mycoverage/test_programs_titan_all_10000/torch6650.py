import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
result = torch.Tensor.floor_divide_(input_tensor, 2)