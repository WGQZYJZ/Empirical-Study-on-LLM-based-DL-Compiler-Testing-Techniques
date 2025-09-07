import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(10, 5)
torch.special.ndtr(data)