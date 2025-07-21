import torch
from torch import nn
from torch.autograd import Variable
x = torch.ones(2, 2, requires_grad=True)
torch.set_grad_enabled(True)
torch.set_grad_enabled(False)
y = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32, requires_grad=True)
with torch.no_grad():
    print((x ** 2).requires_grad)
x = torch.ones(2, 2, requires_grad=True)
y = (x + 2)