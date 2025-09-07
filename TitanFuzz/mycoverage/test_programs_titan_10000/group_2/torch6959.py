import torch
from torch import nn
from torch.autograd import Variable

input = torch.tensor([0.5, 1.5, 2.5])
output = torch.special.sinc(input)