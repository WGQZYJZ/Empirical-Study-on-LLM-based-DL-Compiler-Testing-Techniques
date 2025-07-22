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

    def __init__(self):
        super(Model, self).__init__()

    def forward(query, key, value, dropout_p=0.5):
        key = torch.transpose(key, dim0=-2, dim1=-1)
        dot_product = torch.matmul(query, key)
        scale_factor = torch.sqrt(torch.tensor(query.size(-1)))
        inv_scale_factor = 1.0 / scale_factor
        scaled_dot_product = dot_product * inv_scale_factor
        softmax_dot_product = torch.nn.functional.softmax(scaled_dot_product, dim=scaled_dot_product.dim() - 1)
        final_dot_product = torch.nn.functional.dropout(softmax_dot_product, p=dropout_p)
        result = final_dot_product.matmul(value)
        return result


func = Model().to('cpu')


query = torch.randn(25, 1, 16)

key = torch.randn(25, 16, 2)

value = torch.randn(25, 2, 16)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
matmul(): argument 'input' (position 1) must be Tensor, not Model

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpf4hjmb4p/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpf4hjmb4p/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpf4hjmb4p', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''