import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor(5.0, requires_grad=True)
x = torch.jit.annotate(torch.float32, x)