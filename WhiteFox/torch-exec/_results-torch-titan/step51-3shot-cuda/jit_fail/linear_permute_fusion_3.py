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
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v25 = []
        v15 = []
        (v9, v7) = x1.shape
        v11 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        (v7, v9) = v11.shape
        v12 = v11.permute(0, 2, 1)
        v20 = v12.stride(0, 1)
        v21 = v12.stride(1, 0)
        v17 = v12[0, :, :]
        v19 = v12[1, :, :]
        v16 = v12[2, :, :]
        v27 = v12[3, :, :]
        v13 = v17.contiguous()
        v15.append(v13)
        v18 = v15[0]
        v22 = v18.stride(0, 1)
        v24 = v18.stride(1, 0)
        v23 = v18.data_ptr()
        v25.append((v22, v21))
        return v12




func = Model().to('cuda')



x1 = torch.randn(4, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
too many values to unpack (expected 2)

jit:


from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''