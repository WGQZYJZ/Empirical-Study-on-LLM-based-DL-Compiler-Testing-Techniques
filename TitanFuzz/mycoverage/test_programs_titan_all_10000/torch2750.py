import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3)
y = torch.randn(2, 3)
x = torch.randn(2, 3)
y = torch.randn(2, 3)
x = torch.randn(2, 3)
y = torch.randn(2, 3)
optimizer = torch.optim.NAdam([x, y], lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, momentum_decay=0.004)