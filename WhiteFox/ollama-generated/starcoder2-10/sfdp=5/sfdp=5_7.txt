
import torch
import math
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, dropout_p=0.1):
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) 
        qk  = qk + torch.nn.functional.pad(attn_mask, (0, 0), 'constant', attn_mask[0][-1].item())
        attn_weight  = torch.softmax(qk, dim=-1)
        attn_weight  = torch.dropout(attn_weight, dropout_p=0.5, training=True) 
        output = attn_weight @ value 
        return output


# Initializing the model
m = Model()
 
# Inputs to the model
query  = torch.randn(128, 496)
key    = torch.randn(768, 512)
value   = torch.randn(30720,)
attn_mask  = torch.nn.functional.pad(torch.zeros((32,), device=torch.device('cpu'), dtype=torch.bool), (496-512), 'constant') + True
__output__  = m(query, key, value)
 
