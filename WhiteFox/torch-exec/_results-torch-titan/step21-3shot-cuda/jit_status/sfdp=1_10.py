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
        self.qk = torch.nn.Linear(in_features=768, out_features=768, bias=True)
        self.value = torch.nn.Linear(in_features=768, out_features=768, bias=False)

    def forward(self, x1, x2):
        k = self.qk(x1)
        v = self.value(x1)
        v1 = torch.matmul(x2, k.transpose((- 2), (- 1)))
        v2 = v1.div(0.0625)
        v3 = v2.softmax(dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=0.1, training=True)
        o1 = v4.matmul(v)
        return o1



func = Model().to('cuda')



x1 = torch.randn(2, 768)



x2 = torch.randn(2, 1, 768)


test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpolpn8fyq/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpolpn8fyq', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpolpn8fyq/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''