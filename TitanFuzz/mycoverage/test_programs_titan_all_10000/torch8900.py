import torch
from torch import nn
from torch.autograd import Variable
data = torch.tensor([(- 1.0), 1.0, 2.0])
out = torch.sigmoid(data)