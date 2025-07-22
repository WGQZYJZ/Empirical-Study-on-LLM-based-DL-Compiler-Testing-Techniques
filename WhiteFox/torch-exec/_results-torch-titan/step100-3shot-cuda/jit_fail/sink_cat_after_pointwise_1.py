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

    def __init__(self, hidden_dim=(1024, 512)):
        super().__init__()
        self.module = torch.nn.Sequential(torch.nn.AdaptiveAvgPool1d(7), torch.nn.Conv1d(512, 512, 3), torch.nn.Conv1d(512, 512, 3), torch.nn.Conv1d(512, 512, 3), torch.nn.AdaptiveAvgPool1d(7), torch.nn.Flatten(), torch.nn.Linear(8192, hidden_dim[0]), torch.nn.Linear(hidden_dim[0], hidden_dim[0]), torch.nn.Sigmoid(), torch.nn.Linear(hidden_dim[0], hidden_dim[0]), torch.nn.Linear(hidden_dim[0], hidden_dim[0]), torch.nn.Sigmoid(), torch.nn.Linear(hidden_dim[0], hidden_dim[0]))

    def forward(self, x):
        y = self.module(x)
        y = torch.softmax(y, dim=1)
        return y




func = Model().to('cuda')



x = torch.randn(8, 512, 1024)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x3584 and 8192x1024)

jit:
Failed running call_module L__self___module_6(*(FakeTensor(..., device='cuda:0', size=(8, 3584)),), **{}):
a and b must have same reduction dim, but got [8, 3584] X [8192, 1024].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''