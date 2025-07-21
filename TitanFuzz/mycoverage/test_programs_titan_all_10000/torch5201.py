import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, requires_grad=True)
optimizer = torch.optim.Adamax([input_data], lr=0.01)
optimizer.zero_grad()
input_data.retain_grad()
loss = input_data.sum()
loss.backward()
optimizer.step()