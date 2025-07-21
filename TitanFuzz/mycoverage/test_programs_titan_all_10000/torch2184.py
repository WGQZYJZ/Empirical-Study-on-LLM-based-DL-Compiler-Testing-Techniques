import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(2, 3)
y = torch.rand(2, 3, dtype=torch.float64)
z = torch.rand(2, 3, layout=torch.strided, dtype=torch.float64, device=torch.device('cpu'), requires_grad=True)