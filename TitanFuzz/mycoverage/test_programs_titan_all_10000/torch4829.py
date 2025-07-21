import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(3, 3)
y = torch.rand(3, 3)
torch.use_deterministic_algorithms(mode=True)
z = torch.add(x, y)