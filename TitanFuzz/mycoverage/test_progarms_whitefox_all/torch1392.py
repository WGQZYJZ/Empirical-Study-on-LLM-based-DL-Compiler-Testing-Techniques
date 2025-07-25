import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
      ...
    
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(128, 64, 8)
key = torch.randn(128, 128, 8)
value = torch.randn(128, 128, 8)
