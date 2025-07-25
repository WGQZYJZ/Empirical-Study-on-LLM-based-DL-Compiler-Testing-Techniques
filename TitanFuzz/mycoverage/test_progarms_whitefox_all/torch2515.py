import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, scale_factor, dropout_p):
        super().__init__()
        self.dropout_p = dropout_p
        self.scale_factor = scale_factor
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        scaled_qk = qk.div(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(x2)
        return output

m = Model()
# Initializing the model
m = Model(0.2, 0.3)

# Inputs to the model
x1 = torch.randn(1, 8, 2)
x2 = torch.randn(1, 8, 3)
output = m(x1, x2)

