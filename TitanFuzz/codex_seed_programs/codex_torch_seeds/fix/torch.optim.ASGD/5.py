'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.ASGD\ntorch.optim.ASGD(params, lr=0.01, lambd=0.0001, alpha=0.75, t0=1000000.0, weight_decay=0)\n'
import torch
import torch.nn as nn
from torch.autograd import Variable
from torch.optim import lr_scheduler
import numpy as np
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = Variable(torch.randn(20, 20).double(), requires_grad=False)
target = Variable(torch.randn(10, 20).double(), requires_grad=False)
print('Task 3: Call the API torch.optim.ASGD')
params = [input, target]
learning_rate = 0.01
lambd = 0.0001
alpha = 0.75
t0 = 1000000.0
weight_decay = 0
optimizer = torch.optim.ASGD(params, lr=learning_rate, lambd=lambd, alpha=alpha, t0=t0, weight_decay=weight_decay)
print('optimizer = ', optimizer)