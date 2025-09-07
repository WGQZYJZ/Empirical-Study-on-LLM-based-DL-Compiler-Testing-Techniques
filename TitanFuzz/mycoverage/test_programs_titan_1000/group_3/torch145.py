import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, requires_grad=True)
target = torch.empty(3).random_(2)
loss = torch.nn.functional.binary_cross_entropy_with_logits(input, target)