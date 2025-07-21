import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(3, 5), requires_grad=True)
target = Variable(torch.FloatTensor(3, 5).random_(2))
loss = torch.nn.functional.soft_margin_loss(input, target)
loss.backward()