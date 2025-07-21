import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(10, 10)
y = torch.rand(10, 10)
torch.are_deterministic_algorithms_enabled()