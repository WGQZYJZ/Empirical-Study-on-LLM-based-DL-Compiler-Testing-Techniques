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

    def __init__(self, embedding_size=256, heads=8, dropout_p=0.3, seq_len=512, vocab_len=10000, hidden_size=2048):
        super().__init__()
        self.token_embed = torch.nn.Embedding((vocab_len + 1), embedding_size)
        self.transformer = torch.nn.TransformerEncoderLayer(embedding_size, heads, hidden_size, dropout_p, norm_first=True)
        self.lm_head = torch.nn.Linear(embedding_size, (vocab_len + 1))
        self.positional_embedding = torch.nn.Parameter(torch.randn((seq_len + 1), embedding_size))
        self._init_weights()

    def _init_weights(self):
        initrange = 0.1
        self.token_embed.weight.data.uniform_((- initrange), initrange)
        self.positional_embedding.data.uniform_((- initrange), initrange)

    def forward(self, x1):
        embed = (self.positional_embedding + self.token_embed(x1))
        out = self.transformer(embed)
        return self.lm_head(out)



func = Model().to('cuda')



x1 = torch.randn(1, 512)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected tensor for argument #1 'indices' to have one of the following scalar types: Long, Int; but got torch.cuda.FloatTensor instead (while checking arguments for embedding)

jit:
Failed running call_module L__self___token_embed(*(FakeTensor(..., device='cuda:0', size=(1, 512)),), **{}):
tensors used as indices must be long, int, byte or bool tensors

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''