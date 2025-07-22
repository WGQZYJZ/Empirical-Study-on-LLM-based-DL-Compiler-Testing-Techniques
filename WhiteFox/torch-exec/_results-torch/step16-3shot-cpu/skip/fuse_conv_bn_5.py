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

class Model(torch.jit.ScriptModule):

    def __init__(self, flag):
        super().__init__()
        self.conv = torch.nn.Conv3d(3, 3, 3)
        self.bn = torch.nn.BatchNorm3d(3)

    @torch.jit.script_method
    def foo(self, x1):
        s = self.conv(x1)
        t = self.bn(s)
        return t


flag = 1

func = Model(flag).to('cpu')


x1 = torch.randn(1, 3, 4, 4, 4)

test_inputs = [x1]
