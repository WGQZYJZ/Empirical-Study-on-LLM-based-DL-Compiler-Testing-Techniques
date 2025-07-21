import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([0.2, 0.4, 0.8, 1.0])
output = torch.special.ndtr(input)