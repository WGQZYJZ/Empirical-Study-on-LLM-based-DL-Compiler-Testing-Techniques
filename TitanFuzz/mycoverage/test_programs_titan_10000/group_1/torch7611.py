import torch
from torch import nn
from torch.autograd import Variable

x = torch.tensor([0.0, 0.5, (- 0.5), 1.0, (- 1.0)])
y = torch.arccos(x)