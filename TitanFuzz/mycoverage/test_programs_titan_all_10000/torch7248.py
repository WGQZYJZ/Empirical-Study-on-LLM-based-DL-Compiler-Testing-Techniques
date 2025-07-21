import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([0.0, (- float('inf')), float('inf')])
output = torch.isneginf(input)