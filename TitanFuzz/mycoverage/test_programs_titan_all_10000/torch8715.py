import torch
from torch import nn
from torch.autograd import Variable
a = torch.arange(1, 5, dtype=torch.float32)
b = torch.square(a)
a = torch.arange(1, 5, dtype=torch.float32)
b = torch.sqrt(a)