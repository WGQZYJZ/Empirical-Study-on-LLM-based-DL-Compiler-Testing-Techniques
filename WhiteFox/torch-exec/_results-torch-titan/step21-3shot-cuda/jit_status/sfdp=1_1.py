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

    def __init__(self, n_heads, d_model, p=0.0):
        super().__init__()
        self.n_heads = n_heads
        self.d_model = d_model
        self.p = p
        self.scale_factor = np.sqrt(d_model)

    def forward(self, x1, x2):
        x1_reshape = x1.reshape((x1.shape[0], x1.shape[1], self.n_heads, (- 1)))
        x1_transpose = x1_reshape.transpose(1, 2)
        x1_transpose = x1_transpose.reshape((x1.shape[0], self.n_heads, x2.shape[1], (- 1)))
        x1_transpose = x1_transpose.transpose((- 1), (- 2))
        x1_transpose = x1_transpose.reshape((x1.shape[0], x2.shape[1], (- 1)))
        x2_reshape = x2.reshape((x2.shape[0], x1.shape[1], self.n_heads, (- 1)))
        x2_transpose = x2_reshape.transpose(1, 2)
        x2_transpose = x2_transpose.reshape((x1.shape[0], self.n_heads, x1.shape[1], (- 1)))
        x2_transpose = x2_transpose.transpose((- 1), (- 2))
        x2_transpose = x2_transpose.reshape((x1.shape[0], x1.shape[1], (- 1)))
        q = x1
        k = x2
        v = x2
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        inv_scale_factor = torch.full_like(qk, ((- 1) * self.scale_factor))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.p)
        output = dropout_qk.matmul(v)
        output = output.transpose((- 1), (- 2)).reshape((q.shape[0], 1, (- 1), x2.shape[(- 1)]))
        return output



n_heads = 1
d_model = 1

func = Model(n_heads, d_model).to('cuda')



x1 = torch.randn(1, 64, 32)



x2 = torch.randn(1, 64, 32)


test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp081zeouz/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp081zeouz', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp081zeouz/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''