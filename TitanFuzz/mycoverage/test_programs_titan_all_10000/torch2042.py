import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([1, 3, 2, 3])
output = torch.unique(input)