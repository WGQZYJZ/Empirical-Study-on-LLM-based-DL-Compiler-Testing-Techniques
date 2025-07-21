import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(3, 3, requires_grad=True)
torch.logit(data)