import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(2, 3)
torch.nn.init.uniform_(data, a=0.0, b=1.0)