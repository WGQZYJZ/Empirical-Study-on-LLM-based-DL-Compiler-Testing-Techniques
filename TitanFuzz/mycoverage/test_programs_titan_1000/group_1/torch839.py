import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([(- 3.1415), 3.1415])
y = torch.tensor([2.7183])
z = torch.remainder(x, y)