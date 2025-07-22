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

class Attention_mask(torch.autograd.Function):

    @staticmethod
    def forward(ctx, query, key, value, attn_mask):
        ctx.save_for_backward(query, key, value)
        ctx.attn_mask = attn_mask
        attn_weight = torch.matmul(query, key.transpose(0, 1)) / math.sqrt(query.shape[-1])
        return attn_weight.masked_fill(attn_mask, -float('inf'))

    @staticmethod
    def backward(ctx, grad):
        (query, key, value) = ctx.saved_tensors
        attn_mask = ctx.attn_mask
        attn_weight = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(query.shape[-1])
        attn_weight = attn_weight + attn_mask
        attn_weight.masked_fill_(attn_mask, -float('inf'))
        attn_weight = torch.softmax(attn_weight, dim=-2)
        attn_weight = attn_weight.masked_fill(attn_mask, 0.0)
        attn_grad1 = torch.matmul(attn_weight, grad)
        attn_grad2 = torch.matmul(grad, attn_weight.transpose(0, 1))
        attn_grad2 = attn_grad2.transpose(0, 1)
        query_grad = torch.matmul(attn_grad1, value)
        key_grad = torch.matmul(attn_grad2, value.transpose(0, 1))
        query_grad = query_grad / query.shape[-1]
        key_grad = key_grad / query.shape[-1]
        return (query_grad, key_grad, attn_grad2, None)

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.attn_mask = torch.zeros(64, 64).bool().cuda()

    def forward(self, query, key, value):
        attn_weight1 = Attention_mask.apply(query, key, value, self.attn_mask).cuda()
        attn_weight2 = attn_weight1.masked_fill(self.attn_mask, 0.0)
        return attn_weight2


func = Model().to('cpu')


query = torch.randn(64, 3, 16, 16)

key = torch.randn(64, 3, 16, 16)

value = torch.randn(64, 4, 16, 16)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (64) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x781fa1f96ec0>(*(FakeTensor(..., size=(64, 3, 16, 16)), FakeTensor(..., size=(3, 64, 16, 16))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 47, in forward
  File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''