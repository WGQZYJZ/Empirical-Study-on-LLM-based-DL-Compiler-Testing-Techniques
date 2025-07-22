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
        self.inv_scale_factor = 2.5

    def forward(self, x1, x2):
        v1 = x1.shape[(- 1)]
        v2 = x2.shape[1]
        v3 = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        v4 = v3.div(self.inv_scale_factor).softmax(dim=(- 1))
        v5 = torch.nn.functional.dropout(v4, p=0.1)
        v6 = torch.matmul(v5, x2).permute(0, 2, 1)
        return v6



func = Model().to('cuda')



x1 = torch.randn(1, 3, 8)



x2 = torch.randn(1, 4, 8)


test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpdchcfd2_/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpdchcfd2_', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpdchcfd2_/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''