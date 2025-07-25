import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale_factor = 1 / (64 * 64)
 
    def forward(self, query, key, value, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output
 
m = Model()
# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(4, 64, 32, 32)
key = torch.randn(4, 64, 32, 32)
value = torch.randn(4, 64, 32, 32)
dropout_p = 0.5
__output__=(m(query, key, value, dropout_p))
