import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.ones(2, 2), requires_grad=True)
torch.set_warn_always(True)
torch.set_warn_always(False)