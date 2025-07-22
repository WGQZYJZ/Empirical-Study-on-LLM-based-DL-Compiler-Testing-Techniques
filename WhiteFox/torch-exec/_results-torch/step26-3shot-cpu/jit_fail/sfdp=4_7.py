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

    def __init__(self, num_head, hidden_dim):
        super().__init__()
        self.num_head = num_head
        self.head_dim = d_k = hidden_dim // num_head
        self.scaling = d_k ** (-0.5)
        self.q_net = torch.nn.Linear(hidden_dim, hidden_dim)
        self.k_net = torch.nn.Linear(hidden_dim, hidden_dim)
        self.v_net = torch.nn.Linear(hidden_dim, hidden_dim)
        self.attn_net = torch.nn.Linear(hidden_dim, 1)
        self.proj_net = torch.nn.Linear(hidden_dim, hidden_dim)

    def forward(self, x, x_mask):
        q = self.q_net(x)
        k = self.k_net(x)
        v = self.v_net(x)
        (batch_size, n_seq, d_model) = x.size()
        q = q.view(batch_size, n_seq, self.num_head, self.head_dim).transpose(1, 2)
        k = k.view(batch_size, n_seq, self.num_head, self.head_dim).transpose(1, 2)
        v = v.view(batch_size, n_seq, self.num_head, self.head_dim).transpose(1, 2)
        attn_mask = -torch.ones(n_seq, n_seq).to(x.device)
        if x_mask is not None:
            attn_mask = attn_mask.masked_fill(x_mask.to(torch.bool), float('-inf'))
        attn_weight = torch.softmax(self.scaling * self.attn_net(torch.nn.functional.leaky_relu(q @ k.transpose(-2, -1), 0.1)).transpose(1, 2), -1)
        output = attn_weight @ v
        output = output.transpose(1, 2).reshape(batch_size, n_seq, d_model)
        output = torch.tanh(self.proj_net(output))
        return output


num_head = 1
hidden_dim = 1

func = Model(num_head, hidden_dim).to('cpu')


x = torch.randn(3, 10, 64)

x_mask = torch.tensor([[1, 1, -1, -1, -1, -1, -1, -1, -1, -1]])

test_inputs = [x, x_mask]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (30x64 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(3, 10, 64)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [30, 64] X [1, 1].

from user code:
   File "<string>", line 27, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''