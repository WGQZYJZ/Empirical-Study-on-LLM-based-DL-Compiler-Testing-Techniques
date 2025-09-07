import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.Tensor([[1, 2], [3, 4]]), requires_grad=False)
y = Variable(torch.Tensor([[5, 6], [7, 8]]), requires_grad=False)
loss_fn = torch.nn.MSELoss()
loss = loss_fn(x, y)