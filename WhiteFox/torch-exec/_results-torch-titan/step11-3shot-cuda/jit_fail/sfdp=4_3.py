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

    def __init__(self, n, nhead):
        super().__init__()
        self.w_q = nn.Linear(1, 1, bias=False)
        self.w_kv = nn.Linear(1, nhead, bias=False)
        self.w_o = nn.Linear((nhead + 1), 1)
        self.n = n
        self.nhead = nhead

    def forward(self, q, v, attn_mask):
        q_ = (q * 1)
        kv = (torch.rand(self.n, self.n) * 1)
        q_kv = torch.cat((q_, kv), 1)
        q_ = self.w_q(q_)
        kv = self.w_kv(kv)
        kv = kv.view((- 1), self.nhead, (self.n // self.nhead), 1)
        kv = kv.permute(0, 2, 3, 1)
        q_kv = self.w_o(q_kv)
        q_kv = q_kv.view((- 1), self.nhead, (self.n // self.nhead), 1)
        q_kv = q_kv.permute(0, 2, 3, 1)
        q_ = q_.permute(2, 0, 1).unsqueeze(0)
        attn_weight_ = torch.flatten(torch.matmul(q_, kv), 1)
        attn_weight_ = (attn_weight_ * 1)
        attn_weight = (attn_weight_ * attn_mask)
        attn_weight = self.softmax(attn_weight, 3)
        output = torch.matmul(attn_weight, q_kv)
        (_, n_head, h, _) = output.shape
        output = torch.reshape(output, (h, 1, (n_head * 1)))
        output = self.w_o(output)
        return output




n = 10


nhead = 10


func = Model(n, nhead).to('cuda')


nhead = 10


nhead = 10



attn_mask = torch.ones((nhead, nhead))



n = 10


nhead = 10


batch_size = 1


q = torch.rand(batch_size, nhead, n)



n = 10


nhead = 10


batch_size = 1


v = torch.rand(batch_size, nhead, n)


test_inputs = [attn_mask, q, v]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument tensors in method wrapper_CUDA_cat)

jit:
Failed running call_function <built-in method cat of type object at 0x7796806699e0>(*((FakeTensor(..., device='cuda:0', size=(10, 10)), FakeTensor(..., size=(10, 10))), 1), **{}):
Unhandled FakeTensor Device Propagation for aten.cat.default, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''