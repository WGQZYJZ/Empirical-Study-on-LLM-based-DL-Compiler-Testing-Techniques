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

    def forward(self, query, key, value):
        scale = np.sqrt(query.shape[(- 1)])
        inv_scale = (1.0 / scale)
        matmul1 = torch.matmul(query, torch.transpose(key, (- 2), (- 1)))
        div = matmul1.div(inv_scale)
        softmax = div.softmax(dim=(- 1))
        matmul2 = torch.matmul(softmax, value)
        return matmul2



func = Model().to('cuda')



query = torch.randn(1, 1, 64)



key = torch.randn(1, 128, 64)



value = torch.randn(1, 128, 64)


test_inputs = [query, key, value]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmps624wiyd/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmps624wiyd', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmps624wiyd/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''