import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = torch.tensor([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
result = torch.subtract(x, y)
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])