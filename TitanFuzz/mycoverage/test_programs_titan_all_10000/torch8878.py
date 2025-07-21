import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.Tensor([[1, 2, 3], [4, 5, 6]])
std = torch.std(input_data)