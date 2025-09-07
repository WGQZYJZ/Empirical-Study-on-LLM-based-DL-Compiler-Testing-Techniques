import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, requires_grad=True)
target = torch.randn(2, 3)
loss = torch.nn.functional.poisson_nll_loss(input, target, log_input=True, full=False, size_average=None, eps=1e-08, reduce=None, reduction='mean')