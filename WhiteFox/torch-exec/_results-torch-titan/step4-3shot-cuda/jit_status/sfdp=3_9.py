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

    def forward(self, q, k, v, dropout_p):
        output = torch.matmul(q, k.transpose((- 2), (- 1)))
        output = (output * int(scale_factor))
        output = output.softmax(dim=(- 1))
        output = torch.nn.functional.dropout(output, p=dropout_p)
        output = torch.matmul(output, v)
        return output



func = Model().to('cuda')



q = torch.randn(4, 2, 64)



k = torch.randn(4, 64, 64)



v = torch.randn(4, 64, 64)

dropout_p = 1

test_inputs = [q, k, v, dropout_p]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpx16dpaw0/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpx16dpaw0', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpx16dpaw0/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''