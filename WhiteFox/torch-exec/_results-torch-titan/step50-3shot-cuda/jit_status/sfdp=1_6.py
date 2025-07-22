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

    def forward(self, q1, k2, v3, inv_scale_factor, dropout_p):
        qk1 = torch.matmul(q1, k2.transpose((- 2), (- 1)))
        scaled_qk1 = qk1.div(inv_scale_factor)
        softmax_qk1 = scaled_qk1.softmax((- 1))
        dropout_qk1 = torch.nn.functional.dropout(softmax_qk1, p=dropout_p)
        output = dropout_qk1.matmul(v3)
        return output



func = Model().to('cuda')



q1 = torch.randn(1, 1, 64)



k2 = torch.randn(1, 7, 64)



v3 = torch.randn(1, 7, 64)



inv_scale_factor = torch.tensor(3.14)



dropout_p = torch.tensor(0.5)


test_inputs = [q1, k2, v3, inv_scale_factor, dropout_p]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpffbf8m5t/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpffbf8m5t', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpffbf8m5t/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''