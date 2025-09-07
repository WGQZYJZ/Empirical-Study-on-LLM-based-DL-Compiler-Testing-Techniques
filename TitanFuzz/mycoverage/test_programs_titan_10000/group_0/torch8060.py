import torch
from torch import nn
from torch.autograd import Variable

input = torch.tensor([[True, False], [False, False]])
output = torch.all(input)