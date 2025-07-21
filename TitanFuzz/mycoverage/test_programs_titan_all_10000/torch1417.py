import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3)
target = torch.tensor([1, 0])
loss = torch.nn.functional.nll_loss(input, target)