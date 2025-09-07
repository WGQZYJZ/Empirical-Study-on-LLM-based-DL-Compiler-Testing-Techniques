import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1)
        v2 = torch.nn.functional.dropout(v1)
        v3 = torch.nn.functional.dropout(v2)
        return 123.0 * v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
