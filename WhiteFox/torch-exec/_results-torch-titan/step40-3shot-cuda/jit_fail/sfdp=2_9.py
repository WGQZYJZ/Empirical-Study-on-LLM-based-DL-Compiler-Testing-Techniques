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
        self.num_heads = 4
        self.output_size_per_head = 6
        self.dk = 8
        self.dv = 8
        self.dropout_p = 0.5

    def forward(self, q, k, v, inv_scale_factor, is_training):
        query = q
        key = k
        value = v
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        if should_apply_residual:
            output = output.add(query)
        for i in range(3):
            if should_apply_residual:
                output = output.add(query)
            if should_add_normalization_layer:
                output = output.add(query)
            if should_apply_dropout:
                output = torch.nn.functional.dropout(output, p=self.dropout_p)
            if should_apply_activation_function_inplace:
                output = output.sigmoid()
            if should_apply_activation_function_inplace:
                output = output.clamp(0, 1)
        return output



func = Model().to('cuda')



q = torch.randn(1, 3, 256)



k = torch.randn(1, 4, 384)



v = torch.randn(1, 4, 320)



__inv_scale_factor__ = torch.randint(1, 5, (1,))

inv_scale_factor = 1

test_inputs = [q, k, v, __inv_scale_factor__, inv_scale_factor]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 256] but got: [1, 384].

jit:
Failed running call_function <built-in method matmul of type object at 0x7c16e60699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 256)), FakeTensor(..., device='cuda:0', size=(1, 384, 4))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 256] but got: [1, 384].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''