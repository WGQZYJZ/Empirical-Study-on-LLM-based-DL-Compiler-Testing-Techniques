import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([(- 1), (- 2), 3], dtype=torch.float32)
y = torch.abs(x)