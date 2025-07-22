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

    def __init__(self, num_heads=6):
        super().__init__()
        self.num_heads = num_heads
        self.scale_factor = np.sqrt(self.num_heads)

    def forward(self, q, k, v, dropout_p=0.0):
        qk = torch.mul(torch.matmul(q, k.transpose((- 2), (- 1))), self.scale_factor)
        softmax_qk = torch.nn.functional.softmax(qk, dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output



func = Model().to('cuda')



q = torch.randn(1, 6, 256, 256)



k = torch.randn(1, 6, 256, 256)



v = torch.randn(1, 6, 256, 256)


test_inputs = [q, k, v]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpe31oxif4/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpe31oxif4', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpe31oxif4/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''