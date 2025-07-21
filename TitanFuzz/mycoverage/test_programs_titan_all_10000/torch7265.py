import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([(- 1.0), 1.0, 2.0])
y = torch.nn.functional.relu_(x)