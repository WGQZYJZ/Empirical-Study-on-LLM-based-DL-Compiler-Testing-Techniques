import torch
from torch import nn
from torch.autograd import Variable
logits = torch.rand(10, 2)
tau = 1
hard = False
eps = 1e-10
dim = (- 1)
output = torch.nn.functional.gumbel_softmax(logits, tau, hard, eps, dim)