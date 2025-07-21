import torch
from torch import nn
from torch.autograd import Variable
a = torch.rand(3, 3)
b = torch.rand(3, 3)
torch.are_deterministic_algorithms_enabled()