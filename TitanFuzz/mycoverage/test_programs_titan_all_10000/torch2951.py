import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([False, False, True, True], dtype=torch.bool)
y = torch.tensor([False, True, False, True], dtype=torch.bool)
z = torch.logical_xor(x, y)