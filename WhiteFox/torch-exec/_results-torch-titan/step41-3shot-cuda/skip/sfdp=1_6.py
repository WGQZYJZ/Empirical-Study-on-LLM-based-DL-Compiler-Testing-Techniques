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

    def __init__(self, num_queries: List[int], num_keys: List[int], num_values: List[int]):
        super().__init__()
        self.multi_head_self_attentions = torch.nn.ModuleList([torch.nn.MultiheadAttention(n_q, n_k, n_v, 1, 0) for (n_q, n_k, n_v) in zip(num_queries, num_keys, num_values)])

    def forward(self, x1, x2, x3):
        return [self.multi_head_self_attentions[i](query=x1[i], key=x2[i], value=x3[i])[0] for i in range(len(self.multi_head_self_attentions))]



num_queries = 1
num_keys = 1
num_values = 1
func = Model([16], [24], [24]).to('cuda')



x1 = torch.randn(1, 16, 192, 192)



x2 = torch.randn(1, 16, 192, 192)



x3 = torch.randn(1, 16, 192, 192)


test_inputs = [x1, x2, x3]
