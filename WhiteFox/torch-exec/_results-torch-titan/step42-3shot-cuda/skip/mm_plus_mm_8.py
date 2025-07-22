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



class Model(jit.ScriptModule):

    @torch.jit.script_method
    def forward(self, input1, input2, input3, input4):
        return ((torch.mm(input1, input2) * torch.mm(input3, input4)) // 2)




func = Model().to('cuda')



input1 = torch.randn(100, 100)



input2 = torch.randn(100, 100)



input3 = torch.randn(100, 100)



input4 = torch.randn(100, 100)


test_inputs = [input1, input2, input3, input4]
