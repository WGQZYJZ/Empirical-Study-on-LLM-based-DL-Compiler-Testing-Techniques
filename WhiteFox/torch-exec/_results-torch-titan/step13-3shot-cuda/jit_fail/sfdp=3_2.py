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

    def __init__(self, dim, dropout_p=0.1):
        super().__init__()
        self.linear1 = torch.nn.Linear(dim, dim)
        self.dropout = torch.nn.Dropout(dropout_p)
        self.linear2 = torch.nn.Linear(dim, dim)

    def forward(self, q1, k1, v1):
        q2 = self.linear1(q1)
        q3 = self.dropout(q2)
        q4 = self.linear2(q3)
        k2 = self.linear1(k1)
        k3 = self.dropout(k2)
        k4 = self.linear2(k3)
        v2 = self.linear1(v1)
        v3 = self.dropout(v2)
        v4 = self.linear2(v3)
        q5 = torch.matmul(q4, k4.transpose((- 2), (- 1)))
        v5 = torch.matmul(v4, k4.transpose((- 2), (- 1)))
        scale_factor = (q5.size((- 1)) ** (- 0.5))
        q6 = (torch.matmul(q5, k5) * scale_factor)
        q7 = self.dropout(q6)
        output = torch.matmul(q7, v5)
        return output




dim = 16

func = Model(dim).to('cuda')



dim = 16


q1 = torch.randn(3, dim, requires_grad=True)



dim = 16


k1 = torch.randn(3, dim, requires_grad=True)



dim = 16


v1 = torch.randn(3, dim, requires_grad=True)


test_inputs = [q1, k1, v1]

# JIT_FAIL
'''
direct:
name 'k5' is not defined

jit:
name 'k5' is not defined

from user code:
   File "<string>", line 36, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''