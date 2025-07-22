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
        super(Model, self).__init__()
        self.attention = torch.nn.MultiheadAttention(d_model=512, num_heads=8)

    def forward(self, x1, x2):
        (v1, v2) = self.attention(query=x1, key=x2, value=x2)
        return v1



func = Model().to('cuda')



x1 = torch.randn(1, 4, 512)



x2 = torch.randn(1, 3, 512)


test_inputs = [x1, x2]
