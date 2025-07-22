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
        self.conv_transpose = torch.nn.functional.conv_transpose3d
        self.conv_transpose.requires_grad = True

    def forward(self, x1):
        v1 = self.conv_transpose(x1, None, alpha=0.5, stride=2, padding=4, output_padding=0)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 5, 255, 255, 255)

test_inputs = [x1]
