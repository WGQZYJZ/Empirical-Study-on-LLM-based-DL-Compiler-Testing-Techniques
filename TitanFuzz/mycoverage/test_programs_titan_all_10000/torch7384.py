import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(2, 3)
traced_script_module = torch.jit.trace(torch.sum, x)