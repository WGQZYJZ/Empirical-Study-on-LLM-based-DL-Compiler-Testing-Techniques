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

    def forward(self, query, key, value, input_mask, dropout_p, inv_scale_factor):
        mask = torch.FloatTensor(query.shape[:2]).to(query.device).fill_(1).masked_fill_(input_mask.int(), 0)
        expanded_input_mask = mask.unsqueeze(1).unsqueeze(1)
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        output = output.masked_fill(expanded_input_mask, 0)
        return output



func = Model().to('cuda')



query = torch.randn(4, 8, 4)



key = torch.randn(4, 8, 8)



value = torch.randn(4, 8, 4)



input_mask = torch.tensor([[1, 1, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0], [1, 1, 0, 0]])


key = torch.randn(4, 8, 8)


key = torch.randn(4, 8, 8)



inv_scale_factor = torch.full((8,), 0.5, dtype=key.dtype, device=key.device)

dropout_p = 1

test_inputs = [query, key, value, input_mask, inv_scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
masked_fill only supports boolean masks, but got dtype Int

jit:
Failed running call_method masked_fill_(*(FakeTensor(..., device='cuda:0', size=(2,)), FakeTensor(..., device='cuda:0', size=(4, 4), dtype=torch.int32), 0), **{}):
Attempting to broadcast a dimension of length 4 at -1! Mismatching argument at index 1 had torch.Size([4, 4]); but expected shape should be broadcastable to [1, 2]

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''