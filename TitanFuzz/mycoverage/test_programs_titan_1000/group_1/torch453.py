import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.randn(10, 10))
w = Variable(torch.randn(10, 10), requires_grad=True)
torch.nn.utils.clip_grad_norm_(w, max_norm=1.0)