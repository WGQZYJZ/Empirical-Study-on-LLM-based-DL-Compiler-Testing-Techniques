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
        qk = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        softmax_qk = qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk)
        output = dropout_qk.matmul(x2)
        return output



func = Model().to('cuda')



x1 = torch.randn(16, 50, 1024)



x2 = torch.randn(16, 1024, 256)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [16, 1024] but got: [16, 256].

jit:
Failed running call_function <built-in method matmul of type object at 0x7df1e5a699e0>(*(FakeTensor(..., device='cuda:0', size=(16, 50, 1024)), FakeTensor(..., device='cuda:0', size=(16, 256, 1024))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [16, 1024] but got: [16, 256].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''