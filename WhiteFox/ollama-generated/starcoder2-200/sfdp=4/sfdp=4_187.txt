
import torch

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query):
        key  = torch.randn(1024)
        value = torch.randn(768)
        attn_mask = torch.zeros(35, 900).triu()
        qk  = query @ key.transpose(-2, -1)/ math.sqrt(query.size(-1)) 
        qk  = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight  = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output  = attn_weight @ value # Compute the dot product of the attention weights and the value tensor
        return output
        
# Initializing the model
m  = Model()


# Inputs to the model