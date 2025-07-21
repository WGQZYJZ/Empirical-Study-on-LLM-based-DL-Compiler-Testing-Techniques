import torch
from torch import nn
from torch.autograd import Variable
input = torch.randint(0, 10, (3, 3))
result = torch.isfinite(input)