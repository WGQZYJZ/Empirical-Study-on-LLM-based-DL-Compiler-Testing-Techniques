import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1.0, 2.0, 3.0, 4.0], requires_grad=True)
torch.nn.utils.clip_grad_value_(x, 2.0)