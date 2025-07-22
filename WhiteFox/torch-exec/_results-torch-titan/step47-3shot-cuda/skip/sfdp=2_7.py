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
        self.head = torch.nn.MultiheadAttention(dim=3, embed_dim=5, num_heads=1)

    def forward(self, x1, x2):
        (q, k, v) = self.head.forward_pre_hook_for_query(x1, x2, x2)
        (attn_output, attn_output_weights) = self.head._attn(q, k, v)
        result = self.head.forward_hook_for_output(attn_output, attn_output_weights)
        return result



func = Model().to('cuda')



x1 = torch.randn(3, 5)



x2 = torch.randn(2, 5, 7)


test_inputs = [x1, x2]
