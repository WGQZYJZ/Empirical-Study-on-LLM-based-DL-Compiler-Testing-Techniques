import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])
z = torch.less_equal(x, y)