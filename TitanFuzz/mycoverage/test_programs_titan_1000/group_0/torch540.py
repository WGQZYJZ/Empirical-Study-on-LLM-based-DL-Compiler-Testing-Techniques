import torch
from torch import nn
from torch.autograd import Variable
input = torch.randint(100, (3, 3))
output = torch.triu(input, diagonal=0)