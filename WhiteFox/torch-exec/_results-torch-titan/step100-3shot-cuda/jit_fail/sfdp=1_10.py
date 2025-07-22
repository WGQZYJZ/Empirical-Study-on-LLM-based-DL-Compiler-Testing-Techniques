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
        self.mat1 = torch.nn.Linear(64, 128)
        self.mat2 = torch.nn.Linear(64, 128)
        self.mat3 = torch.nn.Linear(128, 128)

    def forward(self, x1, x2):
        v1 = self.mat1(x1)
        v2 = self.mat2(x2)
        v3 = torch.matmul(v1, v2.transpose((- 2), (- 1)))
        v4 = (v3 / math.sqrt(v1.shape[(- 1)]))
        v5 = torch.nn.functional.softmax(v4, dim=(- 1))
        v6 = torch.nn.functional.dropout(v5, p=dropout_p)
        v7 = torch.matmul(v6, x1)
        return v7



func = Model().to('cuda')



x1 = torch.randn(1, 64)



x2 = torch.randn(1, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
name 'dropout_p' is not defined

jit:
name 'dropout_p' is not defined

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''