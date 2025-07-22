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
        self.attention = torch.nn.MultiheadAttention(d_model=7, num_heads=4)

    def forward(self, x1, x2):
        v1 = self.attention(x1, x2, x2)[0]
        return v1



func = Model().to('cuda')



x1 = torch.randn(4, 5, 7)



x2 = torch.randn(4, 10, 7)


test_inputs = [x1, x2]
