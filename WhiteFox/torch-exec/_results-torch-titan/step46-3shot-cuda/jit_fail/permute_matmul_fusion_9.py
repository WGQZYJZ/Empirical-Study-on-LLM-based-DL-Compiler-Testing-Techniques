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
        y1 = torch.bmm(t1, t2)
        t1 = y1.permute(0, 2, 1)
        r1 = torch.matmul(t1, x2)
        return (y1, r1)




func = Model().to('cuda')



x1 = torch.randn(1, 3, 2)



x2 = torch.randn(1, 3, 2)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 3] but got: [1, 2].

jit:
Failed running call_function <built-in method bmm of type object at 0x7ea1780699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 3)), FakeTensor(..., device='cuda:0', size=(1, 2, 3))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 3] but got: [1, 2].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''