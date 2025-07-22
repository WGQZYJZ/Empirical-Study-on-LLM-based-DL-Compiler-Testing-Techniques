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



class model(torch.nn.Module):

    def __init__(self):
        super(model, self).__init__()

    def forward(self, input, bias):
        l1 = torch.n
        v3 = torch.ne
        t1 = torch.nn.functional.relu
        w2 = torch.nn.functional.mish
        y4 = torch.nn.functional.dropout
        w1 = torch.rand_like(input, dtype=torch.float)
        x1 = (input + bias)
        w4 = torch.rand_like(input, dtype=torch.float)
        x1 = (w2(t1(l1(v3(input, x1, input), input), input)), y4(x1, x1, p_r=0.5))
        return torch.nn.functional.dropout(x1, p_r=0.5)




func = model().to('cuda')



input = torch.randn(1, 2, 2)



bias = torch.randn(1, 2, 2)


test_inputs = [input, bias]

# JIT_FAIL
'''
direct:
module 'torch' has no attribute 'n'

jit:
module 'torch' has no attribute 'n'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''