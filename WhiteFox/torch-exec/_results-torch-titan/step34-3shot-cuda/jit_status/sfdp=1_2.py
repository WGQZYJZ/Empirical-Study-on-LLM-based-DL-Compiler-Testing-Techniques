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
        self.dropout_p = 0.1
        self.scaling_factor = 10

    def forward(self, __input__, __input__1):
        v0 = torch.matmul(__input__, __input__1.transpose((- 2), (- 1)))
        v1 = v0.div(self.scaling_factor)
        v2 = torch.nn.functional.softmax(v1, dim=(- 1))
        v3 = torch.nn.functional.dropout(v2, p=self.dropout_p)
        return v3



func = Model().to('cuda')



query = torch.randn(1, 32, 8)



key = torch.randn(1, 32, 8)


test_inputs = [query, key]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp0914_4v_/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp0914_4v_', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp0914_4v_/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''