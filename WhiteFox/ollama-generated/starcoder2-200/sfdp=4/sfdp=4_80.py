
import torch
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, attn_mask=None, value=None):

        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key
        
        qk  += (attn_mask if isinstance(attn_mask, torch.Tensor) else 0.) # Add the attention mask to the scaled dot product
            
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result

        output   = attn_weight @ value # Compute the dot product of the attention weights and the value
        
        return output

m  = Model()

q  = torch.randn(2048, 768)
k  = torch.randn(1024, 512)
__output__   = m(q, k).shape

