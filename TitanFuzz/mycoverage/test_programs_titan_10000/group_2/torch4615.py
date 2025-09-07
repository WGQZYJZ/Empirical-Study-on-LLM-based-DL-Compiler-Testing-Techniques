import torch
from torch import nn
from torch.autograd import Variable

x = torch.rand(1)
y = torch.rand(1)
torch.are_deterministic_algorithms_enabled()