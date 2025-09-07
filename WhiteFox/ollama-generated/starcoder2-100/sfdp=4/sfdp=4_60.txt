

import torch
import math
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        qk  = (query @ key.transpose(-2, -1)) / math.sqrt(query.size(-1)) 
        qk += torch.randn_like(qk) # Generate random mask
        qk  = torch.softmax(qk, dim=-1) 
        output  = attn_weight@value 
        return output


# Initializing the model
m = MyModel()
 
# Input tensors to the model (same dimensionality)
query = torch.randn(32, 50, 64)
key   = torch.randn(32, 768, 192)
value = torch.randn(32, 50, 768)
 
__output__= m(query, key, value)

