import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))
        inv_scale_factor = torch.tensor([1 / scale_factor], dtype=torch.float32)
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 8, 8, 8)
key = torch.randn(1, 8, 8, 8)
value = torch.randn(1, 8, 8, 8)
scale_factor = 128
dropout_p = 0.1
