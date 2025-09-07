import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange(9, dtype=torch.float32).reshape(3, 3)
y = torch.arange(3, 12, dtype=torch.float32).reshape(3, 3)
z = torch.row_stack((x, y))