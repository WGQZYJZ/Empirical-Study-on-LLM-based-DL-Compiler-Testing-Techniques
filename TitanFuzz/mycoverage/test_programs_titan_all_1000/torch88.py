import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[0.2, 0.3, 0.2, 0.9], [0.1, 0.2, 0.3, 0.4], [0.1, 0.1, 0.2, 0.7]])
y = torch.nonzero(x)