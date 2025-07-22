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
        num_heads = 8
        self.query_projection = torch.nn.Linear(32, 32)
        self.key_projection = torch.nn.Linear(32, 32)
        self.value_projection = torch.nn.Linear(32, 32)
        self.position_embedding = torch.nn.Embedding(42, 32)
        self.dropout = torch.nn.Dropout(0.5)

    def forward(self, keys, query):
        projected_query = self.query_projection(query)
        projected_keys = self.key_projection(keys)
        projected_value = self.value_projection(keys)
        position_embedding_values = self.position_embedding.weight
        if (position_embedding_values.dtype in (torch.float64, torch.complex64)):
            position_embeddings = self.position_embedding(tokens)
            float_type = position_embedding_values.dtype
        else:
            position_embeddings = self.position_embedding(tokens)
            float_type = torch.float32
        attn_weights = ((projected_query @ projected_keys.transpose((- 2), (- 1))) / math.sqrt(projected_query.size((- 1))))
        attn_weights = torch.softmax(attn_weights.float(), dim=(- 1)).to(float_type)
        attn = (attn_weights @ projected_value)
        return attn



func = Model().to('cuda')



keys = torch.randn(1, 16, 32)



query = torch.randn(1, 16, 32)


test_inputs = [keys, query]

# JIT_FAIL
'''
direct:
name 'tokens' is not defined

jit:
name 'tokens' is not defined

from user code:
   File "<string>", line 35, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''