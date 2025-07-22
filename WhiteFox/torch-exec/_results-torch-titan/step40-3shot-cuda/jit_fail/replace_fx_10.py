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

    def forward(self, x, mask):
        o_mask = torch.nn.functional.dropout(mask, p=0.1)
        x = (x * o_mask)
        x = self.lin1(x)
        o_mask = torch.nn.Dropout(0.1)(o_mask)
        x = (x * o_mask)
        return x




func = Model().to('cuda')



x = torch.randn(10, 5)



x = torch.randn(10, 5)


mask = torch.ones_like(x)


test_inputs = [x, mask]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'lin1'

jit:
lin1

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''