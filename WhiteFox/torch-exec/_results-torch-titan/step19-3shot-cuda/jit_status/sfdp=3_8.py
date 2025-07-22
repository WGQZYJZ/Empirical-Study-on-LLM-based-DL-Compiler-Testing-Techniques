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

    def scaled_dot_product(self, query, key, scale_factor=(1.0 / math.sqrt(64))):
        return (query.matmul(key.transpose((- 2), (- 1))) * scale_factor)

    def attention(self, q, k, v, dp=0.5):
        qk = self.scaled_dot_product(q, k)
        v = v.squeeze(1)
        qk_d = torch.nn.functional.dropout(torch.softmax(qk, dim=(- 1)), dp)
        return qk_d.matmul(v).unsqueeze(1)

    def forward(self, q, k, v, dp=0.5):
        t1 = self.attention(q, k, v, dp)
        q = q.squeeze(1)
        t2 = self.attention(q, k, v, dp)
        t3 = (t1 * t2)
        return t3



func = Model().to('cuda')



q = torch.randn(1, 1, 64, 64)



k = torch.randn(1, 1, 64, 64)



v = torch.randn(1, 1, 64, 64)


test_inputs = [q, k, v]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpdh7w3_j9/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpdh7w3_j9', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpdh7w3_j9/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''