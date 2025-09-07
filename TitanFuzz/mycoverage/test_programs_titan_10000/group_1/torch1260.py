import torch
from torch import nn
from torch.autograd import Variable

X = torch.randn(1, 1, 3, 3)
torch.hub.get_dir()