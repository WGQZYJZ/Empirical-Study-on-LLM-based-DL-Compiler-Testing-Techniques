import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[True, True], [False, False]], dtype=torch.bool)
other = torch.tensor([[False, True], [False, False]], dtype=torch.bool)
torch.logical_or(input, other)