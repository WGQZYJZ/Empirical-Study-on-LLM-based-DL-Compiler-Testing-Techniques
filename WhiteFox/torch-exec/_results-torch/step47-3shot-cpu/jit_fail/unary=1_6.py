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
        self.linear1 = torch.nn.Linear(3, 80)
        self.linear2 = torch.nn.Linear(80, 800)
        self.linear3 = torch.nn.Linear(800, 800)
        self.linear4 = torch.nn.Linear(800, 800)
        self.linear5 = torch.nn.Linear(800, 800)
        self.linear6 = torch.nn.Linear(800, 800)
        self.linear7 = torch.nn.Linear(800, 800)
        self.linear8 = torch.nn.Linear(800, 800)
        self.linear9 = torch.nn.Linear(800, 800)
        self.linear10 = torch.nn.Linear(800, 800)
        self.linear11 = torch.nn.Linear(800, 800)
        self.linear12 = torch.nn.Linear(800, 800)
        self.linear13 = torch.nn.Linear(800, 800)
        self.linear14 = torch.nn.Linear(800, 800)
        self.linear15 = torch.nn.Linear(800, 800)
        self.linear16 = torch.nn.Linear(800, 800)
        self.linear17 = torch.nn.Linear(800, 800)
        self.linear18 = torch.nn.Linear(800, 800)
        self.linear19 = torch.nn.Linear(800, 800)
        self.linear20 = torch.nn.Linear(800, 800)
        self.linear21 = torch.nn.Linear(800, 800)
        self.linear22 = torch.nn.Linear(800, 800)
        self.linear23 = torch.nn.Linear(800, 800)
        self.linear24 = torch.nn.Linear(800, 800)
        self.linear25 = torch.nn.Linear(800, 800)
        self.linear26 = torch.nn.Linear(800, 800)
        self.linear27 = torch.nn.Linear(800, 800)
        self.linear28 = torch.nn.Linear(800, 800)
        self.linear29 = torch.nn.Linear(800, 800)
        self.linear30 = torch.nn.Linear(800, 800)
        self.linear31 = torch.nn.Linear(800, 800)
        self.linear32 = torch.nn.Linear(800, 800)
        self.linear33 = torch.nn.Linear(800, 800)
        self.linear34 = torch.nn.Linear(800, 800)
        self.linear35 = torch.nn.Linear(800, 800)
        self.linear36 = torch.nn.Linear(800, 800)
        self.linear37 = torch.nn.Linear(800, 800)
        self.linear38 = torch.nn.Linear(800, 800)
        self.linear39 = torch.nn.Linear(800, 800)
        self.linear40 = torch.nn.Linear(800, 800)
        self.linear41 = torch.nn.Linear(800, 800)
        self.linear42 = torch.nn.Linear(800, 800)
        self.linear43 = torch.nn.Linear(800, 800)
        self.linear44 = torch.nn.Linear(800, 800)
        self.linear45 = torch.nn.Linear(800, 800)
        self.linear46 = torch.nn.Linear(800, 800)
        self.linear47 = torch.nn.Linear(800, 800)
        self.linear48 = torch.nn.Linear(800, 800)
        self.linear49 = torch.nn.Linear(800, 800)
        self.linear50 = torch.nn.Linear(800, 800)
        self.linear51 = torch.nn.Linear(800, 800)
        self.linear52 = torch.nn.Linear(800, 800)
        self.linear53 = torch.nn.Linear(800, 800)
        self.linear54 = torch.nn.Linear(800, 800)
        self.linear55 = torch.nn.Linear(800, 800)
        self.linear56 = torch.nn.Linear(800, 800)
        self.linear57 = torch.nn.Linear(800, 800)
        self.linear58 = torch.nn.Linear(800, 800)
        self.linear59 = torch.nn.Linear(800, 800)
        self.linear60 = torch.nn.Linear(800, 800)
        self.linear61 = torch.nn.Linear(800, 800)
        self.linear62 = torch.nn.Linear(800, 800)
        self.linear63 = torch.nn.Linear(800, 800)
        self.linear64 = torch.nn.Linear(800, 800)
        self.linear65 = torch.nn.Linear(800, 800)
        self.linear66 = torch.nn.Linear(800, 800)
        self.linear67 = torch.nn.Linear(800, 10)
        self.linear68 = torch.nn.Linear(10, 800)
        self.linear69 = torch.nn.Linear(800, 800)
        self.linear70 = torch.nn.Linear(800, 800)
        self.linear71 = torch.nn.Linear(800, 800)
        self.linear72 = torch.nn.Linear(800, 800)
        self.linear73 = torch.nn.Linear(800, 800)
        self.linear74 = torch.nn.Linear(800, 800)
        self.linear75 = torch.nn.Linear(800, 800)
        self.linear76 = torch.nn.Linear(800, 800)
        self.linear77 = torch.nn.Linear(800, 800)
        self.linear78 = torch.nn.Linear(800, 800)
        self.linear79 = torch.nn.Linear(800, 800)
        self.linear80 = torch.nn.Linear(800, 800)
        self.linear81 = torch.nn.Linear(800, 5)

    def forward(self, x1):
        x1 = self.linear1(x1)
        x2 = x1 * 0.5
        x3 = x1 + x1 * x1 * x1 * 0.044715
        x4 = x3 * 0.7978845608028654
        x5 = torch.tanh(x4)
        x6 = x5 + 1
        x7 = x2 * x6
        x1 = self.linear2(x1)
        x2 = x1 * 0.5
        x3 = x1 + x1 * x1 * x1 * 0.044715
        x4 = x3 * 0.7978845608028654
        x5 = torch.tanh(x4)
        x6 = x5 + 1
        x7 = x7 * x6
        x1 = self.linear3(x1)
        x2 = x1 * 0.5
        x3 = x1 + x1 * x1 * x1 * 0.044715
        x4 = x3 * 0.7978845608028654
        x5 = torch.tanh(x4)
        x6 = x5 + 1
        x7 = x7 * x6
        x1 = self.linear4(x1)
        x2 = x1 * 0.5
        x3 = x1 + x1 * x1 * x1 * 0.044715
        x4 = x3 * 0.7978845608028654
        x5 = torch.tanh(x4)
        x6 = x5 + 1
        x7 = x7 * x6
        x1 = self.linear5(x1)
        x2 = x1 * 0.5
        x3 = x1 + x1 * x1 * x1 * 0.044715
        x4 = x3 * 0.7978845608028654
        x5 = torch.tanh(x4)
        x6 = x5 + 1
        x7 = x7 * x6
        x1 = self.linear6(x1)
        x2 = x1 * 0.5
        x3 = x1 + x1 * x1 * x1 * 0.044715
        x4 = x3 * 0.7978845608028654
        x5 = torch.tanh(x4)
        x6 = x5 + 1
        x7 = x7 * x6
        x1 = self.linear7(x1)
        x2 = x1 * 0.5
        x3 = x1 + x1 * x1 * x1 * 0.044715
        x4 = x3 * 0.7978845608028654
        x5 = torch.tanh(x4)
        x6 = x5 + 1
        x7 = x7 * x6
        x1 = self.linear8(x1)
        x2 = x1 * 0.5
        x3 = x1 + x1 * x1 * x1 * 0.044715
        x4 = x3 * 0.7978845608028654
        x5 = torch.tanh(x4)
        x6 = x5 + 1
        x7 = x7 * x6
        x1 = self.linear9(x1)
        x2 = x1 * 0.5
        x3 = x1 + x1 * x1 * x1 * 0.044715
        x4 = x3 * 0.7978845608028654
        x5 = torch.tanh(x4)
        x6 = x5 + 1
        x7 = x7 * x6
        x1 = self.linear10(x1)
        x2 = x1 * 0.5
        x3 = x1 + x1 * x1 * x1 * 0.044715
        x4 = x3 * 0.7978845608028654
        x5 = torch.tanh(x4)
        x6 = x5 + 1
        x7 = x7 * x6
        x1 = self.linear11(x1)
        x2 = x1 * 0.5
        x3 = x1 + x1 * x1 * x1 * 0.044715
        x4 = x3 * 0.7978845608028654
        x5 = torch.tanh(x4)
        x6 = x5 + 1
        x7 = x7 * x6
        x1 = self.linear12(x1)
        x2 = x1 * 0.5
        x3 = x1 + x1 * x1 * x1 * 0.044715
        x4 = x3 * 0.7978845608028654
        x5 = torch.tanh(x4)
        x6 = x5 + 1
        x7 = x7 * x6
        x1 = self.linear13(x1)
        x2 = x1 * 0.5
        x3 = x1 + x1 * x1 * x1 * 0.044715
        x4 = x3 * 0.7978845608028654
        x5 = torch.tanh(x4)
        x6 = x5 + 1
        x7 = x7 * x6
        x1 = self.linear14(x1)
        x2 = x1 * 0.5
        x3 = x1 + x1 * x1 * x1 * 0.044715
        x4 = x3 * 0.7978845608028654
        x5 = torch.tanh(x4)
        x6 = x5 + 1
        x7 = x7 * x6
        x1 = self.linear15(x1)
        x2 = x1 * 0.5
        x3 = x1 + x1 * x1 * x1 * 0.044715
        x4 = x3 * 0.7978845608028654
        x5 = torch.tanh(x4)
        x6 = x5 + 1
        x7 = x7 * x6
        x1 = self.linear16(x1)
        x2



func = Model().to('cpu')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
linear(): argument 'input' (position 1) must be Tensor, not int
'''