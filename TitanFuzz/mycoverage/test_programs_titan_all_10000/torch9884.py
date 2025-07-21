import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 5, requires_grad=True)
target = torch.empty(2, 5).random_(2)
loss = torch.nn.functional.binary_cross_entropy_with_logits(input, target)
weight = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
loss = torch.nn.functional.binary_cross_entropy_with_logits(input, target, weight=weight)