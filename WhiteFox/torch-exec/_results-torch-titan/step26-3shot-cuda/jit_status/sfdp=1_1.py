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

    def __init__(self, head_dim, num_heads, dropout_p=0.1, scale_factor=None):
        super(Model, self).__init__()
        self.dropout_p = dropout_p
        self.head_dim = head_dim
        self.num_heads = num_heads
        self.head_dim = head_dim
        self.scale_factor = scale_factor
        self.w_query = nn.Linear(self.head_dim, self.head_dim)
        self.w_key = nn.Linear(self.head_dim, self.head_dim)
        self.w_value = nn.Linear(self.head_dim, self.head_dim)

    def forward(self, x1, x2):
        query = self.w_query(x1)
        key = self.w_key(x1)
        value = self.w_value(x1)
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        if (self.scale_factor is not None):
            inv_scale_factor = (1 / self.scale_factor)
            scaled_qk = qk.div(inv_scale_factor)
        else:
            scaled_qk = qk
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output



head_dim = 1
num_heads = 1
func = Model(10, 2).to('cuda')



x1 = torch.randn(3, 10)



x2 = torch.randn(1, 10)


test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmphct6s77j/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmphct6s77j', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmphct6s77j/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''