import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange(1, 4, dtype=torch.float)
y = torch.vander(x, 2, False)