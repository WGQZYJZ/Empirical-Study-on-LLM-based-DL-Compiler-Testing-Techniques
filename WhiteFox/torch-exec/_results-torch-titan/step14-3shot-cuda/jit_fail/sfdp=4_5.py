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
        self.query = torch.nn.Linear(4, 6)
        self.key = torch.nn.Linear(5, 8)
        self.value = torch.nn.Sequential(torch.nn.Linear(5, 7), torch.nn.Tanh())

    def forward(self, q, k, v, mask):
        qk = (self.query(q) @ self.key(k).transpose((- 2), (- 1)))
        attn_mask = mask.unsqueeze(1)
        qk = (qk + attn_mask)
        attn_weights = torch.softmax(qk, dim=(- 1))
        output = (attn_weights @ self.value(v))
        return output



func = Model().to('cuda')



q = torch.randn(1, 3, 4)



k = torch.randn(4, 1, 5)



v = torch.randn(4, 1, 5)




mask = torch.tensor([[False, False, True], [False, False, False], [True, True, True]], dtype=torch.bool)


test_inputs = [q, k, v, mask]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [4, 6] but got: [4, 8].

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 6)), FakeTensor(..., device='cuda:0', size=(4, 8, 1))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [4, 6] but got: [4, 8].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''