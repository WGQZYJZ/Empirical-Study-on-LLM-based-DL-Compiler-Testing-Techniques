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

    def forward(self, x1, x2):
        v1 = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        v2 = (v1 * 0.125)
        v3 = (v1 * 0.20884964425119185)
        v4 = v3.softmax(dim=(- 1))
        v5 = torch.nn.functional.dropout(v4, p=0.125)
        output = v5.matmul(x2)
        return output



func = Model().to('cuda')



x1 = torch.randn(2, 8, 4, 4)



x2 = torch.randn(2, 8, 10, 20)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [16, 4] but got: [16, 20].

jit:
Failed running call_function <built-in method matmul of type object at 0x797fcd6699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 8, 4, 4)), FakeTensor(..., device='cuda:0', size=(2, 8, 20, 10))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [16, 4] but got: [16, 20].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''