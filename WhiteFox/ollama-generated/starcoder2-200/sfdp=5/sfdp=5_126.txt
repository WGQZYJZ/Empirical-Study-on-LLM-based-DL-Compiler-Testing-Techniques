
import torch
import math
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        attn  = (query @ key.transpose(-2, -1)) / math.sqrt(query.size(-1))
        attn += self._get_mask() 
        attn   = torch.softmax(attn, dim=-1)
        attn   = torch.dropout(attn, dropout_p=0.5, training=self.training) # apply dropout here
        out    = (attn @ value)
 
        return out
 
    def _get_mask(self):
        attn  = self._get_attn_mask() 
        return attn
 
# Initialize the model
m  = Model()
 
# Inputs to the model
q   = torch.randn(4, 64, 10)
k   = torch.randn(4, 32, 8)
v   = torch.randn(4, 576000, 9)
attn_mask= torch.ones((4, 32), dtype=torch.uint8) # Create an attention mask
 
__output__  = m(q, k, v)

