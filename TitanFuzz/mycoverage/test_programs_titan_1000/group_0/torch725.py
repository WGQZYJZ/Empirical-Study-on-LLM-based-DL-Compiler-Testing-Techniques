import torch
from torch import nn
from torch.autograd import Variable
data = torch.arange(0, 10)
result = torch.randint_like(data, 0, 10)