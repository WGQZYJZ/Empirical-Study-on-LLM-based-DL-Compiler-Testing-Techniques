import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])
z = torch.tensor([7, 8, 9])
tensor_stack = torch.stack((x, y, z))
tensor_concatenate = torch.cat((x, y, z), dim=0)