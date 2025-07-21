import torch
from torch import nn
from torch.autograd import Variable
input = torch.randint(0, 9, (3, 3))
torch.cov(input, correction=1)
torch.cov(input, correction=0)