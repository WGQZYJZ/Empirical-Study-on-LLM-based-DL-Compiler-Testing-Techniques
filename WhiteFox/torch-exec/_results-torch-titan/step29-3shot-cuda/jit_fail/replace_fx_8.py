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
        self.dense1 = torch.nn.Linear(2, 2)
        self.dense2 = torch.nn.Linear(2, 2)
        self.dropout1 = torch.nn.Dropout(0.1)
        self.dropout2 = torch.nn.Dropout(0.2)
        self.dropout3 = torch.nn.Dropout(0.3)

    def forward(self, batch):
        x1 = self.dense1(batch)
        x2 = self.dense2(x1)
        x3 = self.dropout1(x1)
        x4 = self.dropout2(x2)
        x5 = self.dropout3(x2)
        return x2




func = Model().to('cuda')



batch = torch.randn(1, 10)


test_inputs = [batch]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x10 and 2x2)

jit:
Failed running call_module L__self___dense1(*(FakeTensor(..., device='cuda:0', size=(1, 10)),), **{}):
a and b must have same reduction dim, but got [1, 10] X [2, 2].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''