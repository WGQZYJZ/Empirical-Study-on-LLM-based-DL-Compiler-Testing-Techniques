import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1.0, (- 1.0)], [1.0, (- 1.0)]], requires_grad=True)
torch.enable_grad()
y = (x ** 2)
z = ((2 * y) + 3)
z.backward(torch.ones_like(x))
with torch.no_grad():
    print((x ** 2).requires_grad)
y = x.detach()