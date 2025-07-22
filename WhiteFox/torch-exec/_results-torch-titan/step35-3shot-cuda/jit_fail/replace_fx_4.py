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



class model(torch.nn.Module):

    def __init__(self, hidden_size, output_size):
        super(model, self).__init__()
        self.layer1 = torch.nn.Linear(2, hidden_size)
        self.relu = torch.nn.ReLU()
        self.layer2 = torch.nn.Linear(hidden_size, output_size)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, input):
        z1 = self.layer1(input)
        a1 = z1
        z2 = self.relu(a1)
        y1 = self.sigmoid(self.layer2(z2))
        return y1



hidden_size = 1
output_size = 1

func = model(hidden_size, output_size).to('cuda')

input = 1

test_inputs = [input]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_module L__self___layer1(*(1,), **{}):
linear(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''