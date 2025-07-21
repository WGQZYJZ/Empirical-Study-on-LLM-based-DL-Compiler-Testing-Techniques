import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(1, 1, dtype=torch.float)
sin_data = torch.sin(data)