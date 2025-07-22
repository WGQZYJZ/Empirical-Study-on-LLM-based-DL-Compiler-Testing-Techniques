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
        self.token_embed = torch.nn.Embedding(vocab_len + 1, embedding_size)
        self.transformer = torch.nn.TransformerEncoderLayer(embedding_size, heads, hidden_size, dropout_p, norm_first=True)
        self.lm_head = torch.nn.Linear(embedding_size, vocab_len + 1)
        self.positional_embedding = torch.nn.Parameter(torch.randn(seq_len + 1, embedding_size))
        self._init_weights()

    def _init_weights(self):
        initrange = 0.1
        self.token_embed.weight.data.uniform_(-initrange, initrange)
        self.positional_embedding.data.uniform_(-initrange, initrange)

    def forward(self, x1):
        embed = self.positional_embedding + self.token_embed(x1)
        out = self.transformer(embed)
        return self.lm_head(out)


func = Model().to('cpu')


x1 = torch.randn(1, 512)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected tensor for argument #1 'indices' to have one of the following scalar types: Long, Int; but got torch.FloatTensor instead (while checking arguments for embedding)

jit:
Failed running call_function <function embedding at 0x7aa1ca56bca0>(*(FakeTensor(..., size=(1, 512)), Parameter(FakeTensor(..., size=(10001, 256), requires_grad=True)), None, None, 2.0, False, False), **{}):
tensors used as indices must be long, int, byte or bool tensors

from user code:
   File "<string>", line 29, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/sparse.py", line 190, in forward
    return F.embedding(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''