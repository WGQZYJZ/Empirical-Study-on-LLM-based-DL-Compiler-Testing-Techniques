import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(5, 3)
y = torch.zeros(5, 3, dtype=torch.long)
z = torch.tensor([5.5, 3])
x = torch.rand(5, 3)
y = torch.randn_like(x, dtype=torch.float)
x = torch.randint(3, 10, (3, 3))