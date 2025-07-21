import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mode_tensor = torch.Tensor.mode(input_tensor, dim=0, keepdim=False)