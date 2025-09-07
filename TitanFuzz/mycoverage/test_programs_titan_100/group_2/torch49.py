import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange(4, dtype=torch.float32)
y = torch.zeros_like(x)