import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([1.0, 2.0, 3.0, 4.0])
target = torch.tensor([1.0, 1.0, 1.0, 1.0])
loss = torch.nn.functional.poisson_nll_loss(input, target, log_input=True, full=False, size_average=None, eps=1e-08, reduce=None, reduction='mean')