import torch
from torch import nn
from torch.autograd import Variable
input1 = torch.randn(4, 3, requires_grad=True)
input2 = torch.randn(4, 3, requires_grad=True)
input3 = torch.randn(4, 3, requires_grad=True)
loss = torch.nn.functional.triplet_margin_loss(input1, input2, input3, margin=1.0, p=2, eps=1e-06, swap=False, size_average=None, reduce=None, reduction='mean')