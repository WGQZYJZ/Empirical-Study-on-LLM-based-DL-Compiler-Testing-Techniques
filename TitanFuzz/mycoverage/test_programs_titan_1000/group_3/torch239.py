import torch
from torch import nn
from torch.autograd import Variable
data = torch.rand(3, 4)
torch.is_grad_enabled()
torch.set_grad_enabled(False)
torch.is_grad_enabled()
torch.set_grad_enabled(True)
torch.is_grad_enabled()