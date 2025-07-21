import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange(1, 5, dtype=torch.float32)
y = torch.tensor([3.0, 4.0, 4.0, 4.0])
z = torch.greater(x, y)