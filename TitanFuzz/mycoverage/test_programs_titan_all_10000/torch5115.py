import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(1, 3, 4, 5)
arcsin_data = torch.arcsin(data)