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
        self.ln_0 = torch.nn.LayerNorm(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.ln_0(x1)
        v2 = ((v1 - x2) + 0.5)
        return v2



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 3, 64, 64)


test_inputs = [x1, x2]
