import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 5, requires_grad=True)
output = torch.randn_like(input)
output = torch.randn_like(input, dtype=torch.float)
output = torch.randn_like(input, dtype=torch.float, layout=torch.strided, device='cpu', requires_grad=True)