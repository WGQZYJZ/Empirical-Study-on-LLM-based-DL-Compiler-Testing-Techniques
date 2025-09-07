import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange(1, 10, dtype=torch.float32).view(3, 3)
y = torch.matrix_power(x, 3)