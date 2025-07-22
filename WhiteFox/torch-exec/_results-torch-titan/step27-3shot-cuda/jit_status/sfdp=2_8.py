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

    def __init__(self, num_heads):
        super().__init__()
        self.query = torch.randn(4, 13, 64)
        self.key = torch.randn(4, 17, 64)
        self.value = torch.randn(4, 17, 64)

    def forward(self, query, key, value, dropout_p):
        inv_scale_factor = 0.1
        self.softmax_qk = torch.matmul(query, key.transpose((- 2), (- 1))).div(inv_scale_factor).softmax(dim=(- 1))
        self.dropout_qk = torch.nn.functional.dropout(self.softmax_qk, p=dropout_p)
        output = torch.matmul(self.dropout_qk, value)
        return output



num_heads = 1

func = Model(num_heads).to('cuda')



query = torch.randn(4, 7, 64)



key = torch.randn(4, 5, 64)



value = torch.randn(4, 5, 64)

dropout_p = 1

test_inputs = [query, key, value, dropout_p]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp43ntp03i/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp43ntp03i', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp43ntp03i/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''