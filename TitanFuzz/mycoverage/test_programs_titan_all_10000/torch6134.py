import torch
from torch import nn
from torch.autograd import Variable
tensor = torch.randn(2, 3)
tensor = torch.reshape(tensor, (3, 2))