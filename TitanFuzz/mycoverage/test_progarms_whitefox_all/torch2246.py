import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, scorer):
        v1 = torch.matmul(x1, x2.transpose(-2, -1))
        v2 = v1 * scorer
        v3 = v2.softmax(dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=0.987654321)
        v5 = torch.matmul(v4, x2)
        return v5   
 
m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 1)
x2 = torch.randn(1, 1, 1)
scorer = torch.tensor(0.5, requires_grad=True)
