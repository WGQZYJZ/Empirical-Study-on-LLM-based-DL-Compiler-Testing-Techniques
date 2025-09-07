
import torch
from torch import nn
 
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = (2 ** -0.5)
 
    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output

# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(8, 64, 512)
key  = torch.randn(8, 3072, 512)
value  = torch.randn(8, 64, 512)
 
__output__  = m(query, key, value)

