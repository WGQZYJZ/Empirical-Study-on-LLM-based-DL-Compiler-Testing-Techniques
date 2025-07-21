import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float32, requires_grad=True)
y = torch.tensor([2, 2, 2, 2, 2], dtype=torch.float32, requires_grad=True)
z = torch.gt(x, y)
x = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float32, requires_grad=True)
y = torch.tensor([2, 2, 2, 2, 2], dtype=torch.float32, requires_grad=True)
z = torch.gt(x, y)