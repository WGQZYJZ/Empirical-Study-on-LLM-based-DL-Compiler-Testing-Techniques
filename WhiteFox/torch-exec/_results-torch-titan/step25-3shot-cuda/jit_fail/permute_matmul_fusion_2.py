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

    def forward(self, x1, x2):
        x1 = x1.reshape(4, 2)
        x2 = x2.reshape(4, 2)
        x3 = (x1.t() @ x2)
        x3 = (x2 @ x1.t())
        x3 = (x1.t() @ x1)
        x3 = (x1 @ x1.t())
        x3 = (x2.t() @ x1)
        x3 = (x1 @ x2.t())
        x4 = x3.transpose(0, 1)
        x4 = x3.transpose((- 1), (- 2))
        x4 = x3.transpose(1, (- 1))
        x4 = x3.t()
        v1 = (x2 @ x1.t())
        v2 = (x1.t() @ x2)
        v3 = (x1.t() @ x1)
        v4 = (x1 @ x1.t())
        v5 = (x2.t() @ x1)
        v6 = (x1 @ x2.t())
        v7 = x1.t()
        v8 = v8.permute(0, 2, 1)
        v8 = v8.permute(0, 2, 1)
        v8 = v8.permute(0, 2, 1)
        v9 = v9.permute((- 1), (- 2), (- 3))
        v9 = v9.permute(0, 2, 1)
        v9 = v9.permute(0, 2, 1)
        v9 = v9.permute(0, 2, 1).squeeze((- 1))
        v1 = v1.permute(0, 2, 1)
        v1 = v1.permute(0, 2, 1)
        v1 = v1.permute(0, 2, 1)
        v1 = v1.permute((- 1), (- 2), (- 3))
        v1 = v1.permute(0, 2, 1)
        v1 = v1.permute(0, 2, 1)
        v1 = v1.permute(0, 2, 1).squeeze((- 1))
        x2 = x2.reshape(2, 4)
        x2 = x2.reshape(4, 2)
        x2 = x2.t()
        v1 = x1.t()
        v2 = x1.t()
        v1 = v1.transpose(0, 1)
        v1 = v1.transpose((- 1), (- 2))
        v1 = v1.transpose(1, (- 1)).squeeze((- 1))
        v2 = v2.transpose(0, 1)
        v2 = v2.transpose((- 1), (- 2))
        v2 = v2.transpose(1, (- 1)).squeeze((- 1))
        x1 = x1.reshape(2, 4)
        x1 = x1.reshape(4, 2)
        v1 = x1.t()
        v2 = x1.t()
        v1 = v1.transpose(0, 1)
        v1 = v1.transpose((- 1), (- 2))
        v1 = v1.transpose(1, (- 1)).squeeze((- 1))
        x1 = x1.transpose(0, 1)
        v2 = v2.transpose(0, 1)
        v2 = v2.transpose((- 1), (- 2))
        v2 = v2.transpose(1, (- 1)).squeeze((- 1))
        v1 = x1.t()
        v2 = x1.t()
        v1 = v1.transpose(0, 1)
        v1 = v1.transpose((- 1), (- 2))
        v1 = v1.transpose(1, (- 1)).squeeze((- 1))




func = Model().to('cuda')



x1 = torch.randn(2, 4)



x2 = torch.randn(2, 4)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
local variable 'v8' referenced before assignment

jit:
local variable 'v8' referenced before assignment
'''