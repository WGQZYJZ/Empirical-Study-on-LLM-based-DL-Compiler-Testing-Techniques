import torch
from torch import nn
from torch.autograd import Variable
logits = torch.randn(3, 5)
output = torch.nn.functional.gumbel_softmax(logits, tau=1, hard=False, eps=1e-10, dim=(- 1))
logits = torch.randn(3, 5)