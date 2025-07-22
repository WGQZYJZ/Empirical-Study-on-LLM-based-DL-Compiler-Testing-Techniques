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
        t1 = x1.permute(0, 2, 1)
        t2 = x2.permute(0, 2, 1)
        y1 = t2.permute(0, 2, 1)
        t3 = torch.bmm(t1, t2)
        z1 = torch.bmm(t3, y1)
        z1 = torch.matmul(y1, torch.tensor([[(- 1), 0, 1]]))
        z2 = torch.bmm(t3, y1)
        z2 = torch.matmul(y1, torch.tensor([[1, (- 2), (- 1)]]))
        z3 = y1.detach().add(z1, alpha=2)
        return (z1, z2, z3)




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)



x2 = torch.randn(1, 2, 2)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat2 in method wrapper_CUDA_mm)

jit:
Failed running call_function <built-in method matmul of type object at 0x7634724699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)), FakeTensor(..., size=(1, 3), dtype=torch.int64)), **{}):
a and b must have same reduction dim, but got [2, 2] X [1, 3].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''