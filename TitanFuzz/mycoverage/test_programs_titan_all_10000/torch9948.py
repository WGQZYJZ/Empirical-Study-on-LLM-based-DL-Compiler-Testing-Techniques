import torch
from torch import nn
from torch.autograd import Variable
logits = torch.rand(3, 5)
torch.nn.functional.gumbel_softmax(logits, tau=1, hard=False, eps=1e-10, dim=(- 1))
torch.nn.functional.gumbel_softmax(logits, tau=1, hard=True, eps=1e-10, dim=(- 1))
torch.nn.functional.gumbel_softmax(logits, tau=1, hard=True, eps=1e-10, dim=0)