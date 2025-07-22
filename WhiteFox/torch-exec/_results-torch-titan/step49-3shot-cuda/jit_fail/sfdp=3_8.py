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
        super(Model, self).__init__()

    def forward(self, __input__0, __input__1):
        v0 = torch.matmul(__input__0, __input__1.transpose((- 2), (- 1)))
        v1 = (v0 * 0.125)
        v2 = F.softmax(v1, dim=(- 1))
        v3 = torch.nn.functional.dropout(v2, p=0.1, training=True)
        output = torch.matmul(v3, __input__0)
        return output



func = Model().to('cuda')



x1 = torch.randn(32, 32, 64)



x2 = torch.randn(32, 64, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [32, 64] but got: [32, 32].

jit:
Failed running call_function <built-in method matmul of type object at 0x72af43e699e0>(*(FakeTensor(..., device='cuda:0', size=(32, 32, 64)), FakeTensor(..., device='cuda:0', size=(32, 32, 64))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [32, 64] but got: [32, 32].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''