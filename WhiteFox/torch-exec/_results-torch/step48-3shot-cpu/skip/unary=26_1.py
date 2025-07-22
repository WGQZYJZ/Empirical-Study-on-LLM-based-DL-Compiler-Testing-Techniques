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
        self.conv_t = torch.nn.ConvTranpose2d(12, 12, (5, 8), 1, 0)

    def forward(self, input8):
        out = self.conv_t(input8)
        mask = out > 0
        mul = out * -0.9
        out = torch.where(mask, out, mul)
        mask = out > 0
        out = torch.where(mask, out, out.sum())
        out = torch.nn.functional.adaptive_avg_pool2d(out, (1, 1))
        return out



func = Model().to('cpu')


input8 = torch.randn(2, 12, 41, 21)

test_inputs = [input8]
