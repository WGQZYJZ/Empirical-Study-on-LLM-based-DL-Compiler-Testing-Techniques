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

    def forward(self, input_tensor):
        q = torch.randn([1, 6, 5]).transpose(1, 2)
        k = torch.randn([1, 6, 10])
        v = torch.randn([1, 6, 10])
        output = torch.matmul(q.transpose(1, 2), k) / math.sqrt(k.shape[-1])
        output += torch.randn([1, 12, 12])
        output = torch.softmax(output, -1)
        output = torch.softmax(output, -1)
        output = torch.matmul(output, v)
        return output


func = Model().to('cpu')


x1 = torch.randn([1, 12, 5])

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 5] but got: [1, 6].

jit:
Failed running call_function <built-in method matmul of type object at 0x7df4ae796ec0>(*(FakeTensor(..., size=(1, 6, 5)), FakeTensor(..., size=(1, 6, 10))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 5] but got: [1, 6].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''