
import torch
import torch.nn.functional as F

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.randn(1, 10)
        self.key  = torch.randn(5, 8)
        self.value  = torch.randn(5, 32)

    def forward(self): 
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk  += attn_mask  # Add the attention mask to the scaled dot product
        attn_weight  = F.softmax(qk, dim=-1)   # Apply softmax to the result 
        output  = attn_weight @ value    # Compute the dot product of the attention weights and the value tensor 
        return output, qk

m  = Model()

