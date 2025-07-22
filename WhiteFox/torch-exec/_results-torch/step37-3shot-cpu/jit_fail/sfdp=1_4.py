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

    def __init__(self, input, hidden):
        super().__init__()
        self.hidden_size = hidden
        self.output_size = input // hidden

    def forward(self, x):
        v = x.view(-1, self.hidden_size, self.output_size)
        q = v.permute(0, 2, 1).contiguous().view(-1, self.output_size, self.hidden_size)
        k = v.contiguous().view(-1, self.output_size, self.hidden_size)
        qk = torch.nn.functional.softmax((q * k).sum(-1), -1)
        output = torch.einsum('bxy,bxz->byz', v, qk.unsqueeze(-1)).view(x.size())
        return output


input = 1
hidden = 1
func = Model(512, 64).to('cpu')


x1 = torch.randn(32, 512, 8, 8)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
einsum(): subscript x has size 8 for operand 1 which does not broadcast with previously seen size 64

jit:
Failed running call_function <function einsum at 0x7fbc17080040>(*('bxy,bxz->byz', FakeTensor(..., size=(2048, 64, 8)), FakeTensor(..., size=(2048, 8, 1))), **{}):
einsum(): subscript x has size 8 for operand 1 which does not broadcast with previously seen size 64

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''