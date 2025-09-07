import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.ones(2, 2), requires_grad=True)
model = torch.nn.Sequential(torch.nn.Linear(2, 2), torch.nn.ReLU(), torch.nn.Linear(2, 2))
y = model(x)
y.backward(torch.ones(2, 2))