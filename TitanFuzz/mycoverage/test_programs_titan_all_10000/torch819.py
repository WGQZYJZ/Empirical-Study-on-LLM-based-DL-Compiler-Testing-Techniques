import torch
from torch import nn
from torch.autograd import Variable
window_length = 10
periodic = True
dtype = torch.float32
layout = torch.strided
device = torch.device('cpu')
requires_grad = False
window = torch.bartlett_window(window_length, periodic, dtype=dtype, layout=layout, device=device, requires_grad=requires_grad)