import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([1.0, 0.0, (- 1.0)])
other = torch.tensor([0.0, 1.0, 0.0])
torch.atan2(input, other)