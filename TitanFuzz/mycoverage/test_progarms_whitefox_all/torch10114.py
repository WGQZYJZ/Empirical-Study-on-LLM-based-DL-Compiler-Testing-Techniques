import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v = torch.mm(x1, x2)
        for loopVar1 in range(10):
            v = torch.mm(x1, x2)
            for loopVar2 in range(10):
                v = torch.mm(x1, x2)
                for loopVar3 in range(10):
                    v = torch.mm(x1, x2)
                    for loopVar4 in range(10):
                        v = torch.mm(x1, x2)
                        for loopVar5 in range(10):
                            v = torch.mm(x1, x2)
        return torch.cat([v, v], 1)
m = Model()
# Inputs to the model
x1 = torch.randn(4, 4)
x2 = torch.randn(4, 4)
