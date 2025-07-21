import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.randn(3, 5), requires_grad=True)
torch.nn.utils.clip_grad_norm_(x, max_norm=2.0, norm_type=2.0, error_if_nonfinite=False)