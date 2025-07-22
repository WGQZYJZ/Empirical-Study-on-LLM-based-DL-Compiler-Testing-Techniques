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

    def __init__(self, n_head, dim_model):
        super().__init__()
        self.n_head = n_head
        self.dim_model = dim_model
        self.inv_scale_factor = dim_model ** (-0.5)
        self.dropout_p = 0.0
        self.w_query = torch.nn.Linear(dim_model, dim_model)
        self.w_key = torch.nn.Linear(dim_model, dim_model)
        self.w_value = torch.nn.Linear(dim_model, dim_model)

    def forward(self, x1, x2, mask):
        query = self.w_query(x1)
        key = self.w_key(x2)
        value = self.w_value(x2)
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output


n_head = 32
dim_model = 512
func = Model(n_head, dim_model).to('cpu')


x1 = torch.randn(2, 64, 512)

x2 = torch.randn(2, 4096, 512)

n_head = 32
mask = torch.randn(2, n_head, 64, 4096)

test_inputs = [x1, x2, mask]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp540cv2do/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp540cv2do/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp540cv2do', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''