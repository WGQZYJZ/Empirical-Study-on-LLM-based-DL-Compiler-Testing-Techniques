import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Parameter(torch.randn(8, 5, 8))
    def forward(self, x1):
        q = x1
        k = x1.transpose(-2, -1)
        v = x1
        inv_scale = math.sqrt(k.size(1))
        scaled_dot_product = torch.matmul(q, k) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(v)
        return output
m = Model()
# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
