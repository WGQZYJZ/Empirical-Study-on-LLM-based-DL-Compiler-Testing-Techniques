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



class Module(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, Q, K, V, mask):
        qk = ((Q @ K.transpose((- 2), (- 1))) / math.sqrt(Q.size((- 1))))
        qk = (qk + mask)
        weights = torch.softmax(qk, dim=(- 1))
        return (weights @ V)




func = Module().to('cuda')



q = torch.randn(1, 64, 56, 56)



k = torch.randn(1, 64, 56, 56)



v = torch.randn(1, 64, 56, 56)



mask = (torch.rand(1, 56, 56) > 0.7).fill_((- 1000000000.0))


test_inputs = [q, k, v, mask]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpp7tfpsri/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpp7tfpsri', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpp7tfpsri/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''