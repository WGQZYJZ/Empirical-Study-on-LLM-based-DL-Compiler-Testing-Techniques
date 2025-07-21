import torch
from torch import nn
from torch.autograd import Variable
input = torch.arange(1, 11)
reps = (2, 5)
output = torch.tile(input, reps)