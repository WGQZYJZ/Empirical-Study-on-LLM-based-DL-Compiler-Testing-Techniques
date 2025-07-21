'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adadelta\ntorch.optim.Adadelta(params, lr=1.0, rho=0.9, eps=1e-06, weight_decay=0)\n'
import torch
from torch import nn
from torch import optim
from torch.autograd import Variable
import numpy as np
inputs = Variable(torch.Tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]))
labels = Variable(torch.LongTensor([0, 1]))
optimizer = optim.Adadelta(params=[inputs], lr=1.0, rho=0.9, eps=1e-06, weight_decay=0)