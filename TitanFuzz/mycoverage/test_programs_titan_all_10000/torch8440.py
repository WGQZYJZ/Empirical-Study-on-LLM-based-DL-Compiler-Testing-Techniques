import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = torch.tensor([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
condition = (x > 5)
z = torch.where(condition, x, y)