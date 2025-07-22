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
        self.num_heads = 10
        self.transformer = torch.nn.Transformer(d_model=255, nhead=self.num_heads)

    def forward(self, x1, x2):
        return self.transformer(x=x1, attn_mask=x2)



func = Model().to('cuda')



x1 = torch.randn(1, 255, 256)



x2 = torch.randn(1, 256, 256)


test_inputs = [x1, x2]
