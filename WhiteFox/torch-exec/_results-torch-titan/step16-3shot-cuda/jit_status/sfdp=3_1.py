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
        self.dropout = torch.nn.Dropout(p=0.5)

    def forward(self, q, k, v, scale):
        dropout_qk = self.dropout(torch.softmax((torch.matmul(q, k.transpose((- 2), (- 1))) * scale), dim=(- 1)))
        return torch.matmul(dropout_qk, v)



func = Model().to('cuda')



q = torch.randn(64, 25, (2 * 3085))



k = torch.randn(64, 25, (2 * 3085))



v = torch.randn(64, 25, (2 * 3085))

scale = 1

test_inputs = [q, k, v, scale]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp99an_str/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp99an_str', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp99an_str/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''