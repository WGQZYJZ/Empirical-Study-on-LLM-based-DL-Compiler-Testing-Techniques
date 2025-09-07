
import torch
import torch.nn as nn
 
class AttentionLayer(torch.nn.Module):
    def __init__(self, key, query, value):
        super().__init__()
        
        # Compute the dot product of the query and key
        self._attn = torch.nn.Linear(key, 1)
        self._v    = nn.Parameter(value / math.sqrt(query.size(-1)))
 
    def forward(self, query, key, value):
        qk = (self._attn(key) @ query).transpose(dim0=-2, dim1=-3)
        qk  = qk + attn_mask  # Add the attention mask to the scaled dot product
        
        # Apply softmax to the result and compute the dot product of the attention weights and value
        attn_weight = torch.softmax(qk, dim=-1) @ self._v
        return attn_weight
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self._query  = nn.Parameter(torch.randn([8,32])) # Parameter for query
        self._key   = nn.Parameter(torch.randn([4,10])) # Parameter for key
        self._value = nn.Parameter(torch.randn([7,64,19*5+2*2, 128])) # Parameter for value
        self._attn_layer = AttentionLayer(self._key, self._query, self._value)
 
    def forward(self):
       return self._attn_layer(self._query.unsqueeze(-3), self._key.unsqueeze(-3).transpose(-2,-1), self._value)
 
