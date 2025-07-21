import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([5, 25, 125])
y = torch.tensor([3, 15, 75])
result = torch.lcm(x, y)