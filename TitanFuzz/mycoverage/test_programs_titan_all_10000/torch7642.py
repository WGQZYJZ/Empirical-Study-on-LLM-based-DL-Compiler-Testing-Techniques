import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(4, 4)
min_value = (- 0.5)
max_value = 0.5
y = torch.clamp(x, min=min_value, max=max_value)