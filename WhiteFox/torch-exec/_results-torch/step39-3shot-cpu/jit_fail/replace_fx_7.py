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

class SimpleRNNModel(torch.nn.Module):

    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim):
        super(SimpleRNNModel, self).__init__()
        self.emb_layer = torch.nn.Embedding(vocab_size, embedding_dim)
        self.rnn_layer = torch.nn.RNN(input_size=embedding_dim, hidden_size=hidden_dim, nonlinearity='relu')
        self.linear_layer = torch.nn.Linear(hidden_dim, output_dim)
        self.hidden_dim = hidden_dim
        self.softmax = torch.nn.Softmax(dim=1)

    def init_hidden(self):
        return torch.zeros(1, 1, self.hidden_dim)

    def forward(self, x):
        emb = self.emb_layer(x.long())
        v = self.rnn_layer(emb)
        v = self.linear_layer(v)
        return self.softmax(v)


vocab_size = 1
embedding_dim = 1
hidden_dim = 1
output_dim = 1

func = SimpleRNNModel(vocab_size, embedding_dim, hidden_dim, output_dim).to('cpu')


x1 = torch.tensor([[1, 15, 2]])

test_inputs = [x1]

# JIT_FAIL
'''
direct:
index out of range in self

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp4rcc6z6k/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp4rcc6z6k/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp4rcc6z6k', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''