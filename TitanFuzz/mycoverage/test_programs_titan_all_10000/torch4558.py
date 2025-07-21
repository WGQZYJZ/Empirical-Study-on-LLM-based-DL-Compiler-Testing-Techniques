import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([(- 1), 0, 1, 2, 3, 4, 5], dtype=torch.float)
y = torch.square(x)