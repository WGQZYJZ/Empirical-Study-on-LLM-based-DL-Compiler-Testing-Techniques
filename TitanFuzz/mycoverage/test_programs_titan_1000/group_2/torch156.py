import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(100)
window = torch.bartlett_window(100)