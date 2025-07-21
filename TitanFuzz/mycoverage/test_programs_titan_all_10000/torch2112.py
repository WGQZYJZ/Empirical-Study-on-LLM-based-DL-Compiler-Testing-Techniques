import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(5, 5)
y = torch.rand(5, 5)
torch.are_deterministic_algorithms_enabled()