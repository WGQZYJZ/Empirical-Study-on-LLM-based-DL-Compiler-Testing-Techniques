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

    def forward(self, Q16, K16, V, mask):
        qk = ((Q16 @ K16.transpose((- 2), (- 1))) / math.sqrt(Q16.size((- 1))))
        qk = (qk + mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ V)
        return output




func = Model().to('cuda')



Q = torch.randn(1, 3, 512)



K = torch.randn(1, 3, 512)



V = torch.randn(1, 512, 56)




mask = (torch.rand(1, 56) > 0.7).fill_(float((- 100000000.0)))


test_inputs = [Q, K, V, mask]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (56) at non-singleton dimension 2

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 3)), FakeTensor(..., device='cuda:0', size=(1, 56), dtype=torch.bool)), **{}):
Attempting to broadcast a dimension of length 56 at -1! Mismatching argument at index 1 had torch.Size([1, 56]); but expected shape should be broadcastable to [1, 3, 3]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''