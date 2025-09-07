import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.Tensor([[1, 2], [3, 4]])
output = torch.full(size=input_data.size(), fill_value=10)