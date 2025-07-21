import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(3, requires_grad=True)
optimizer = torch.optim.AdamW([x], lr=0.1)
optimizer.step()