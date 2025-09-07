import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([0.0, 1.0, (- 1.0), 0.0001, (- 0.0001), 88.8])
y = torch.sinh(x)