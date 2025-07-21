import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([(- 1), 0, 1])
y = torch.tanh(x)