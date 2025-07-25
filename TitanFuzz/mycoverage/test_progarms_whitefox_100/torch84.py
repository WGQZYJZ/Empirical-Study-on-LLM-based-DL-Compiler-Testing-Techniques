import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, dropout_p):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        inv_scale_factor = torch.sqrt(torch.tensor(32., dtype=x1.dtype, device=device).float())
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(x2)
        return output

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 256, 64)
x2 = torch.randn(1, 512, 64)
dropout_p = 0.
