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

    def __init__(self, inv_scale_dim, dropout_p):
        super().__init__()
        self.i_s = inv_scale_dim

    def forward(self, query, key, value, dropout_p):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        inv_s = torch.rsqrt(torch.tensor([qk.size()[(- 1)]]))
        s_qk = qk.div(inv_s.to(qk))
        do_qk = torch.nn.functional.dropout(s_qk, dropout_p)
        out = do_qk.matmul(value)
        return out



inv_scale_dim = 1

dropout_p = 0.8

func = Model(3, 0.0).to('cuda')



size = 5


length = 4


seq = 3


batch = 2


query = torch.randn(batch, seq, length, size)



size = 5


length = 4


seq = 3


batch = 2


key = torch.randn(batch, seq, length, size)



size = 5


length = 4


seq = 3


batch = 2


value = torch.randn(batch, seq, length, size)

dropout_p = 1

test_inputs = [query, key, value, dropout_p]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpm7k_au9d/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpm7k_au9d', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpm7k_au9d/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''