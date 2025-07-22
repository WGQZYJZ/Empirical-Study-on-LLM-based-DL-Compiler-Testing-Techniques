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

    def forward(self, q2, k1, v4):
        s1 = q2.matmul(k1.transpose((- 2), (- 1)))
        s2 = (s1 * scale_factor)
        s3 = torch.nn.functional.softmax(s2, dim=(- 1))
        s4 = torch.nn.functional.dropout(s3, p=dropout_p)
        o1 = s4.matmul(v4)
        return o1



func = Model().to('cuda')



q2 = torch.randn(1, 13, 64)



k1 = torch.randn(1, 37, 51)



v4 = torch.randn(1, 37, 64)


test_inputs = [q2, k1, v4]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 64] but got: [1, 51].

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(1, 13, 64)), FakeTensor(..., device='cuda:0', size=(1, 51, 37))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 64] but got: [1, 51].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''