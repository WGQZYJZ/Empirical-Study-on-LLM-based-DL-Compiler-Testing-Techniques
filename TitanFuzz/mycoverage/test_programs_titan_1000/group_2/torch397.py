import torch
from torch import nn
from torch.autograd import Variable
x = torch.ones(2, 2, requires_grad=True)
y = (x + 2)
z = ((y * y) * 3)
out = z.mean()
out.backward()