import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3)
torch.are_deterministic_algorithms_enabled()