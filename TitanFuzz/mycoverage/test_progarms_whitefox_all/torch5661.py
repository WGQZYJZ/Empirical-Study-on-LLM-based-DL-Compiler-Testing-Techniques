import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, scale_factor, dropout_p):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(x2)
        return output

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 10, 20)
x2 = torch.randn(1, 10, 20)
scale_factor = torch.randn(1, 1, 1)
dropout_p = 0.1
