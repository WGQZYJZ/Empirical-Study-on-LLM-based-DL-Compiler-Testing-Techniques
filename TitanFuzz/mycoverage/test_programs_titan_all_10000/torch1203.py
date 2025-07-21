import torch
from torch import nn
from torch.autograd import Variable
x = torch.Tensor([[1, 2, 3], [4, 5, 6]])
y = torch.Tensor([[7, 8, 9], [10, 11, 12]])
z = torch.stack([x, y])
z1 = torch.stack([x, y], dim=1)