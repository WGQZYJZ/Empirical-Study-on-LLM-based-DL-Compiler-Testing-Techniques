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

    def __init__(self, input_dim=128, num_heads=8, dropout_p=0.0):
        super().__init__()
        self.query = torch.nn.Linear(input_dim, input_dim, bias=False)
        self.key = torch.nn.Linear(input_dim, input_dim, bias=False)
        self.value = torch.nn.Linear(input_dim, input_dim)
        self.softmax_qk = torch.nn.Softmax(dim=(- 1))
        self.dropout = torch.nn.Dropout(dropout_p)
        self.output = torch.nn.Linear(input_dim, input_dim)

    def forward(self, x):
        q = self.query(x)
        k = self.key(x)
        v = self.value(x)
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = (qk / np.sqrt(k.size((- 1))))
        softmax_qk = self.softmax_qk(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(v)
        return self.output(output)



func = Model(input_dim=256, num_heads=8, dropout_p=0.2).to('cuda')



x = torch.randn(568, 256)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmplthb6wmd/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmplthb6wmd', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmplthb6wmd/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''