import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor(1.0, requires_grad=True)
w = torch.tensor(2.0, requires_grad=True)
b = torch.tensor(3.0, requires_grad=True)
with torch.no_grad():
    y = ((x * w) + b)
    print(y)