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



class Model2(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(128, 128, bias=False)
        self.key = torch.nn.Linear(128, 128, bias=False)
        self.value = torch.nn.Linear(128, 128, bias=False)
        self.softmax = torch.nn.Softmax(dim=(- 1))

    def forward(self, query, key, value):
        inv_scale_factor = math.sqrt(128)
        q = self.query(query)
        k = self.key(key)
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = self.softmax(scaled_qk)
        p = 0.25
        dropout_soft = torch.nn.functional.dropout(softmax_qk, p=p)
        return self.value(dropout_soft.matmul(value))



func = Model2().to('cuda')



query = torch.randn(5, 128)



key = torch.randn(5, 128)



value = torch.randn(5, 128)


test_inputs = [query, key, value]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpojvr_rs3/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpojvr_rs3', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpojvr_rs3/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''