import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout_p = 0.9
    
    def forward(self, q, k, v):
        qk = torch.matmul(q, k.transpose(-2, -1))
        inv_scale_factor = v.size(-1) ** -0.5
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p, training=self.training)
        output = dropout_qk.matmul(v)
        return output

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(1, 16, 10, 20)
k = torch.randn(1, 32, 20, 40)
v = torch.randn(1, 32, 20, 40)
