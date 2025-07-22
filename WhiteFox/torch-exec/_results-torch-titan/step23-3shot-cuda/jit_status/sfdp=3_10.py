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
        self.softmax = torch.nn.Softmax(dim=(- 1))
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, query, key, value, scale_factor):
        v1 = torch.matmul(query, key.transpose((- 2), (- 1)))
        v2 = v1.mul(scale_factor)
        v3 = self.softmax(v2)
        v4 = self.dropout(v3)
        output = torch.matmul(v4, value)
        return output



func = Model().to('cuda')



query = torch.randn(2, 3, 4)



key = torch.randn(2, 3, 4)



value = torch.randn(2, 3, 4)

scale_factor = 1

test_inputs = [query, key, value, scale_factor]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmptgwk5_5w/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmptgwk5_5w', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmptgwk5_5w/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''