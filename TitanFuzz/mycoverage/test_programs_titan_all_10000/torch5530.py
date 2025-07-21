import torch
from torch import nn
from torch.autograd import Variable
data = torch.arange(1, 4)
data = torch.arange(1, 4, step=2)
data = torch.arange(1, 4, step=2, dtype=torch.float32)