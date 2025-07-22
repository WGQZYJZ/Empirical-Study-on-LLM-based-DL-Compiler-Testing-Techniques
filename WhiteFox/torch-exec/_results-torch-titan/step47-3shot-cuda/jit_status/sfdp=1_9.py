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

    def __init__(self, dim):
        super().__init__()
        self.dim = dim

    def forward(self, q, k, v, scale_factor=None, dropout_p=0.0):
        q_k = torch.matmul(q, k.transpose((- 2), (- 1)))
        if (scale_factor is not None):
            q_k = q_k.div(scale_factor)
        softmax_qk = torch.nn.functional.softmax(q_k, dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1, training=self.training)
        output = dropout_qk.matmul(v)
        return output



dim = 1
func = Model(2).to('cuda')



q = torch.randn(1, 5, 2)



k = torch.randn(1, 6, 2)



v = torch.randn(1, 6, 2)


test_inputs = [q, k, v]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpqti__vco/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpqti__vco', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpqti__vco/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''