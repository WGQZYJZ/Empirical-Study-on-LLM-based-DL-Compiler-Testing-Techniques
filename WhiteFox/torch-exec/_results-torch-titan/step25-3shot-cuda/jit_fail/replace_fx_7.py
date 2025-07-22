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

    def forward(self, x1):
        u1 = torch.nn.functional.dropout(x1, p)
        u2 = torch.nn.functional.dropout(x1, p=0.0)
        return (u1 - u2)




func = Model().to('cuda')



x1 = torch.randn(1, 2, 3, 5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'p' is not defined

jit:
name 'p' is not defined

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''