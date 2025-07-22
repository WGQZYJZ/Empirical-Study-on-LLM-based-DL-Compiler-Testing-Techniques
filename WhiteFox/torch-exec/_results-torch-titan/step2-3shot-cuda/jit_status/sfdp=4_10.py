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

    def __init__(self, n_head=4, n_query_dim=32, n_key_dim=32, n_value_dim=32, n_vocab_size=50):
        super().__init__()
        self.scale = math.sqrt(n_query_dim)
        self.query = torch.nn.Linear(n_query_dim, n_key_dim)
        self.key = torch.nn.Linear(n_key_dim, n_key_dim)
        self.value = torch.nn.Linear(n_value_dim, n_value_dim)

    def forward(self, q, k, v, attn_mask=None):
        q = self.query(q)
        k = self.key(k)
        v = self.value(v)
        attn_weight = ((q @ k.transpose((- 2), (- 1))) / self.scale)
        if (attn_mask is not None):
            attn_weight = (attn_weight + attn_mask)
        attn_prob = torch.nn.functional.softmax(attn_weight, dim=(- 1))
        output = (attn_prob @ v)
        return output



func = Model().to('cuda')



q = torch.randn(3, 4, 32)



k = torch.randn(3, 7, 32)



v = torch.randn(3, 7, 32)


test_inputs = [q, k, v]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpevx6zrih/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpevx6zrih', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpevx6zrih/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''