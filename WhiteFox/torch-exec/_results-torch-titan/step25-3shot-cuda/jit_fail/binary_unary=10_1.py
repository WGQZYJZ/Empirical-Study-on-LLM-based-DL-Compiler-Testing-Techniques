import os
import torch
import torch.nn.functional as F
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
import math
import torch as th
import torch.linalg as la
from torch.nn import Parameter
import torch.linalg as linalg



class MyModule1(torch.nn.Module):

    def __init__(self, hidden_size, num_layers):
        super().__init__()
        self.lstm1 = torch.nn.ModuleList()
        self.lstm2 = torch.nn.ModuleList()
        self.lstm3 = torch.nn.ModuleList()
        self.fc1 = torch.nn.Linear(hidden_size, (hidden_size * 4))
        self.gru = torch.nn.GRU((hidden_size * 4), hidden_size, num_layers=num_layers, dropout=0.2, bidirectional=True)
        for i in range(2, 3):
            layer = torch.nn.LSTM((hidden_size * 4), hidden_size, batch_first=True)
            setattr(self, ('lstm%i' % i), layer)

    def forward_gru(self, x, h):
        self.gru.flatten_parameters()
        return self.gru(x, h)[0]

    def forward(self, x):
        num_layers = len(self.lstm1)
        seq = x.shape[1]
        h = x.new_zeros(((num_layers * 2), x.shape[0], hidden_size))
        c = x.new_zeros(((num_layers * 2), x.shape[0], hidden_size))
        for i in range(num_layers):
            (x, hc) = getattr(self, ('lstm%i' % (i + 1)))(x, (h[(2 * i):((2 * i) + 2), :, :].contiguous(), c[(2 * i):((2 * i) + 2), :, :].contiguous()))
            (h[(2 * i):((2 * i) + 2), :, :], c[(2 * i):((2 * i) + 2), :, :]) = hc
        x = F.relu(self.fc1(x))
        return self.forward_gru(x, h)



hidden_size = 1
num_layers = 1

func = MyModule1(hidden_size, num_layers).to('cuda')



x1 = torch.randn(1, 8, 10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x10 and 1x4)

jit:
Failed running call_module L__self___fc1(*(FakeTensor(..., device='cuda:0', size=(1, 8, 10)),), **{}):
a and b must have same reduction dim, but got [8, 10] X [1, 4].

from user code:
   File "<string>", line 40, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''