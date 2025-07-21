import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(3, 5), requires_grad=True)
target = Variable(torch.FloatTensor(3, 5).random_(2))
loss = torch.nn.BCEWithLogitsLoss()
output = loss(input, target)
output.backward()
input = Variable(torch.randn(3, 5), requires_grad=True)