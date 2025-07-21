import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 4)
indices = torch.tensor([0, 2])
y = torch.index_select(x, dim=0, index=indices)
z = torch.zeros(2, 4)
torch.index_select(x, dim=0, index=indices, out=z)