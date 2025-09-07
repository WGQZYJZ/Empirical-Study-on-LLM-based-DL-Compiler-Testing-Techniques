# pylint: disable=E1101
import torch

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.nn.functional.dropout(x1) 
        v2  = torch.rand_like(v1)
        return v2
