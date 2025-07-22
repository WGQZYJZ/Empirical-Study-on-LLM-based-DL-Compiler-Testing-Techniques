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
        super().__init__()

    def forward(self, x1):
        q = self.q(x1).view((- 1), num_heads, (input_depth // num_heads), ((input_depth // num_heads) * 3))
        k = self.k(x1).view((- 1), num_heads, (input_depth // num_heads), ((input_depth // num_heads) * 3))
        v = self.v(x1).view((- 1), num_heads, (input_depth // num_heads), ((input_depth // num_heads) * 3))
        scale_factor = (1 / math.sqrt((input_depth // num_heads)))
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v).view((- 1), (num_heads * (input_depth // num_heads)), (3 * 3))
        return output

    @torch.jit.export
    def q(self, x1):
        q = torch.nn.functional.max_pool2d(x1, (3, 3), stride=(2, 2))
        return q

    @torch.jit.export
    def k(self, x1):
        q = torch.nn.functional.avg_pool2d(x1, (3, 3), stride=(2, 2))
        return q

    @torch.jit.export
    def v(self, x1):
        q = torch.nn.functional.adaptive_avg_pool2d(x1, (3, 3))
        return q



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'num_heads' is not defined

jit:
name 'num_heads' is not defined

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''