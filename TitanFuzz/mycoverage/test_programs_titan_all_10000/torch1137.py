import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 2, 3, dtype=torch.float)
y = torch.arcsinh(x)
x = torch.randn(1, 2, 3, dtype=torch.float)
y = torch.unsqueeze(x, dim=0)
x = torch.randn(1, 2, 3, dtype=torch.float)
y = torch.squeeze(x)
x = torch.randn(1, 2, 3, dtype=torch.float)
y = torch.transpose(x, dim0=0, dim1=1)