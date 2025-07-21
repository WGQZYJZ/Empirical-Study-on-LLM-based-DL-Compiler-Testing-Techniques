import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([3.0, 4.0])
y = torch.tensor([5.0, 6.0])
torch.hypot(x, y)
x = torch.tensor([3.0, 4.0])
y = torch.tensor([5.0, 6.0])
torch.hypot(x, y, out=torch.empty(2))
x = torch.tensor([3.0, 4.0])
y = torch.tensor([5.0, 6.0])
torch.hypot(x, y, out=torch.empty(2))