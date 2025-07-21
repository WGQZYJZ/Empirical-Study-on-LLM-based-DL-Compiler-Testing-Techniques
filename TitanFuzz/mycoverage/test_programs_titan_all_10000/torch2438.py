import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(3, 5, requires_grad=True)
torch.nn.utils.clip_grad_norm_(a, max_norm=1.0)