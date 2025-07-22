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

    def __init__(self, config):
        super().__init__()
        self.proj_q = torch.nn.Linear(config.d_model, (config.d_head * config.n_head))
        self.proj_k = torch.nn.Linear(config.d_model, (config.d_head * config.n_head))
        self.proj_v = torch.nn.Linear(config.d_model, (config.d_head * config.n_head))

    def forward(self, x1, x2, x3):
        q = self.proj_q(x1)
        k = self.proj_k(x2)
        v = self.proj_v(x3)
        q = q.view((- 1), x1.size(1), self.config.n_head, self.config.d_head)
        k = k.view((- 1), x2.size(1), self.config.n_head, self.config.d_head)
        v = v.view((- 1), x3.size(1), self.config.n_head, self.config.d_head)
        return (q, k, v)



config = 1

func = Model(config).to('cuda')



x1 = torch.randn(4, 720)



x2 = torch.randn(2, 720)



x3 = torch.randn(2, 720)


test_inputs = [x1, x2, x3]
