import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.matmul(x1, x2.transpose(-2, -1))
        v2 = v1 * 1
        v3 = v2.softmax(dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=0.1)
        v5 = torch.matmul(v4, x2)
        return v5

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 512, 768)
x2 = torch.randn(32, 511, 768)
