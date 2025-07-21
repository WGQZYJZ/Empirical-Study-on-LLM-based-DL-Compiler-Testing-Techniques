import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(2, 2)
y = torch.rand(2, 2)
torch.are_deterministic_algorithms_enabled()