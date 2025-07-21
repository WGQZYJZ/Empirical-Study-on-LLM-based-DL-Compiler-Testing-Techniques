import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
y = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
z = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
loss = torch.nn.MarginRankingLoss(margin=0.0, size_average=None, reduce=None, reduction='mean')
output = loss(x, y, z)