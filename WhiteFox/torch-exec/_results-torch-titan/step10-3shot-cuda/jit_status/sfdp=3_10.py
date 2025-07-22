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
        self.dropout = torch.nn.Dropout(0.1)

    def forward(self, q, k, v):
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        dropout_qk = self.dropout(qk)
        output = torch.matmul(dropout_qk, v)
        return output



func = Model().to('cuda')



q = torch.randn(1, 8, 96, 96)



k = torch.randn(1, 8, 96, 96)



v = torch.randn(1, 8, 96, 96)


test_inputs = [q, k, v]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp_cvdiy6e/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp_cvdiy6e', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp_cvdiy6e/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''