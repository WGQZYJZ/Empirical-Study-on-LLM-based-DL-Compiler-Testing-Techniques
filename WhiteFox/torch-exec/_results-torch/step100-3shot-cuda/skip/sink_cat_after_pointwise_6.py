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

class Model(transformers.PreTrainedModel):

    def __init__(self):
        super().__init__(transformers.RobertaConfig())
        self.operator_1 = torch.nn.Linear(in_features=5, out_features=3)
        self.operator_2 = torch.nn.Linear(in_features=6, out_features=3)

    def forward(self, x):
        o1 = self.operator_1(x)
        o2 = self.operator_2(x)
        o = torch.cat([o1, o2], dim=1)
        y = o.view(o.shape[0], -1)
        return y



func = Model().to('cuda')


x = torch.randn(2, 3, 5)

test_inputs = [x]
