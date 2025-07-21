import torch
from torch import nn
from torch.autograd import Variable
data = torch.tensor([(- 1), 0, 1])
out = torch.tan(data)