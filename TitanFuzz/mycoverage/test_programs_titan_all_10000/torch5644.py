import torch
from torch import nn
from torch.autograd import Variable
tensor_a = torch.tensor([[1, 2, 3], [4, 5, 6]])
tensor_b = torch.tensor([[7, 8, 9], [10, 11, 12]])
tensor_cat = torch.cat((tensor_a, tensor_b), dim=0)