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
        self.linear0 = torch.nn.Linear(8, 4)
        self.linear1 = torch.nn.Linear(4, 2)

    def forward(self, k, v, q):
        w = self.linear0(k)
        b = self.linear1(q)
        w_b = (w * b)
        w_b_sum = torch.sum(w_b, dim=(- 1))
        w_b_sum_exp = torch.exp(w_b_sum)
        w_b_sum_exp_sum = torch.sum(w_b_sum_exp, dim=(- 1))
        w_b_sum_exp_sum_inv = (1 / w_b_sum_exp_sum)
        result = torch.sum((w * ((b / w_b_sum_exp) * w_b_sum_exp_sum_inv)), dim=(- 1))
        return result



func = Model().to('cuda')



query = torch.randn(1, 2, 8)



key = torch.randn(1, 5, 8)

k = 1

test_inputs = [query, key, k]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_module L__self___linear1(*(1,), **{}):
linear(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''