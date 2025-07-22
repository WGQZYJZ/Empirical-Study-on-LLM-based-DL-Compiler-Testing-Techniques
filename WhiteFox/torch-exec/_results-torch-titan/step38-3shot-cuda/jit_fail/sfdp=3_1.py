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
        self.dropout_p = 0.5
        self.scale_factor = np.sqrt((1.0 / 512.0))
        self.qk_proj = torch.nn.Linear(512, 512)
        self.value_proj = torch.nn.Linear(512, 512)
        self.tanh = torch.nn.Tanh()
        self.softmax_qk = torch.nn.Softmax(dim=(- 1))

    def forward(self, x1, x2):
        qk = self.tanh(self.qk_proj(x1))
        qk = self.tanh(self.value_proj(x2))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = self.softmax_qk(scaled_qk)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



x1 = torch.randn(1, 512)



x2 = torch.randn(1, 512)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat2 in method wrapper_CUDA_mm)

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(1, 512)), FakeTensor(..., size=(2, 5))), **{}):
a and b must have same reduction dim, but got [1, 512] X [2, 5].

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''