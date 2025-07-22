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



class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(64, 10)
        self.fc2 = torch.nn.Linear(10, 100)
        self.fc3 = torch.nn.Linear(100, 64)

    def forward(self, input, other):
        x = self.fc1(input)
        x = torch.relu(x)
        x = self.fc2(x)
        x = torch.relu(x)
        x = torch.add(x, other)
        x = self.fc3(x)
        x = torch.relu(x)
        return x



func = Model().to('cuda')



input = torch.randn(128, 64)



other = torch.randn(128, 64)


test_inputs = [input, other]

# JIT_FAIL
'''
direct:
The size of tensor a (100) must match the size of tensor b (64) at non-singleton dimension 1

jit:
Failed running call_function <built-in method add of type object at 0x7c182fc699e0>(*(FakeTensor(..., device='cuda:0', size=(128, 100)), FakeTensor(..., device='cuda:0', size=(128, 64))), **{}):
Attempting to broadcast a dimension of length 64 at -1! Mismatching argument at index 1 had torch.Size([128, 64]); but expected shape should be broadcastable to [128, 100]

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''