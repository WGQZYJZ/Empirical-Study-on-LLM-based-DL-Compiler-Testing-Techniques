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
        self.key = torch.nn.Linear(3, 5)
        self.value = torch.nn.Linear(3, 5)
        self.query = torch.nn.Linear(3, 5)

    def forward(self, x1):
        k = self.key(x1)
        v = self.value(x1)
        q = self.query(x1)
        qk = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
        mask4 = np.tril(np.ones((3, 3))).astype('int')
        mask5 = to_tensor(mask4)
        v4 = torch.softmax(qk, dim=-1) * mask5
        v5 = v4 @ v
        return v5


func = Model().to('cpu')


x1 = torch.randn(1, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'to_tensor' is not defined

jit:
NameError: name 'to_tensor' is not defined

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''