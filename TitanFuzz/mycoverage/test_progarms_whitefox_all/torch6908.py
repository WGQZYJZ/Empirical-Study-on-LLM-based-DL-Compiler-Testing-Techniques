import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, query, key, value):
        inv_scale_factor = 1.0 / math.sqrt(query.size(-1))
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.3)
        output = dropout_qk.matmul(value)
        return output

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 64, 256)
key = torch.randn(1, 64, 256)
value = torch.randn(1, 64, 256)
