import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1.0, 2.0, 3.0])
y = torch.sigmoid(x)
y = torch.sigmoid(torch.tensor([1, 2, 3]))