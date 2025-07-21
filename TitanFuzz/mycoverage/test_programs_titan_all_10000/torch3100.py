import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([(- 3.0), (- 2.0), (- 1.0), 0.0, 1.0, 2.0, 3.0])
y = torch.special.exp2(x)