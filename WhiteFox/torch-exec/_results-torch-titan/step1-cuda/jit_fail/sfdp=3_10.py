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

    def forward(self, x):
        x1 = (x * x)
        x2 = self.dropout(x1)
        out = x2.matmul(value)
        return out



func = Model().to('cuda')



x = torch.randn(1, 1, 8)


test_inputs = [x]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'dropout'

jit:
dropout

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''