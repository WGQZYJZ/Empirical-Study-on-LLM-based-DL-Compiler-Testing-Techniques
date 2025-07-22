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

    def __init__(self, n_queries=8, n_keys=8, n_values=8, n_head=8, dropout_p=0.2):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(n_head, n_queries, 101))
        self.key = torch.nn.Parameter(torch.randn(n_head, n_keys, 101))
        self.value = torch.nn.Parameter(torch.randn(n_head, n_values, 101))
        self.softmax = torch.nn.Softmax()
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, x2):
        q = self.query.unsqueeze(0).unsqueeze(0).contiguous()
        k = self.key.unsqueeze(0).contiguous()
        v = self.value.unsqueeze(0).contiguous()
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        inv_scale_factor = (1 / np.sqrt(np.prod(qk.shape[(- 2):])))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(v)
        return output.squeeze(0)



func = Model().to('cuda')



x2 = torch.randn(1, 3, 64, 64)


test_inputs = [x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpo62rmqrw/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpo62rmqrw', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpo62rmqrw/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''