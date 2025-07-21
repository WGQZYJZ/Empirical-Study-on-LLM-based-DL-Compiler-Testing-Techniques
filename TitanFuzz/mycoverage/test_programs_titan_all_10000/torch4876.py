import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 3)
torch.are_deterministic_algorithms_enabled()