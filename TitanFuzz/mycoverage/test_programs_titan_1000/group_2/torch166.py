import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 2)
y = torch.randn(2, 2)
torch.use_deterministic_algorithms(True)
z = (x + y)
torch.use_deterministic_algorithms(False)
z = (x + y)
torch.use_deterministic_algorithms(True)
z = (x + y)
torch.use_deterministic_algorithms(False)
z = (x + y)
torch.use_deterministic_algorithms(True)
z = (x + y)