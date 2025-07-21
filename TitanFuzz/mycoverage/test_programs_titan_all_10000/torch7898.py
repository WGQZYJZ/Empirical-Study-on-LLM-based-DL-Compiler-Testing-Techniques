import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([(- 10.0), 0.0, 10.0])
y = torch.special.expit(x)