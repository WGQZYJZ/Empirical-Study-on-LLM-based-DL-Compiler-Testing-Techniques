import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
  
    def forward(self, query, key, value, scale_factor, dropout_p=0.0):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output

# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 350, 100)
key = torch.randn(1, 100, 200)
value = torch.randn(1, 350, 200)
scale_factor = torch.randn(1, 350, 200)
