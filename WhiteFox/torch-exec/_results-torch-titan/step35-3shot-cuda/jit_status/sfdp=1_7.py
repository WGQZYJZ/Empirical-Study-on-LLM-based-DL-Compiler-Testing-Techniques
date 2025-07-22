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

    def __init__(self, n_dim, n_hid, dropout_p):
        super().__init__()
        self.n_hid = n_hid
        self.dropout_p = dropout_p
        self.query = torch.nn.Parameter(torch.randn(n_dim, n_hid))
        self.key = torch.nn.Parameter(torch.randn(n_dim, n_hid))
        self.value = torch.nn.Parameter(torch.randn(n_dim, n_hid))
        self.inv_scale_factor = torch.nn.Parameter(torch.tensor((1.0 / np.sqrt(n_hid))))

    def forward(self, x1):
        qk = torch.matmul(self.query, self.key.transpose(0, 1))
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(self.value)
        return output



n_dim = 1
n_hid = 1

dropout_p = 0.5

func = Model(64, 32, dropout_p).to('cuda')



x1 = torch.randn(6, 64)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp5xsusrqx/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp5xsusrqx', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp5xsusrqx/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''