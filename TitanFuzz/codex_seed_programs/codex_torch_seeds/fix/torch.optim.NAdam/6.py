'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.NAdam\ntorch.optim.NAdam(params, lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, momentum_decay=0.004)\n'
import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable
x = Variable(torch.randn(100, 1), requires_grad=True)
y = Variable(torch.randn(100, 1), requires_grad=True)
optimizer = optim.NAdam([x, y], lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, momentum_decay=0.004)
print(optimizer)