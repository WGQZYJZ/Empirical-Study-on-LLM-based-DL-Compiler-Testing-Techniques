import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
split_size = 2
split_tensor = torch.split(input_tensor, split_size)
split_size = 2
split_tensor = torch.split(input_tensor, split_size, dim=1)