import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, q, k, v, inv_scale_factor, p):
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(1, 128, 64)
k = torch.randn(1, 128, 64)
v = torch.randn(1, 128, 64)
inv_scale_factor = 1/math.sqrt(128)
p = 0.2
