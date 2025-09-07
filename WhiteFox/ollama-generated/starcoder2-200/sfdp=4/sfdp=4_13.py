
import torch
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = (query @ key.transpose(-2,-1)) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        v1 += attn_mask                                                   # Add the attention mask to the scaled dot product
        v2  = torch.softmax(v1, dim=-1)                                     # Apply softmax to the result
        v3  = v2 @ value                                                  # Compute the dot product of the attention weights and the value 
        return v3


# Initializing the model<|end_of_model|>
m  = Model()

# Inputs to the model<|end_of_inputs|>
query  = torch.randn(10,64)
key    = torch.randn(10,528,37,9)
value  = torch.randn(10,528,37,37)
attn_mask  = torch.rand((10,528))
__output__  = m(query, key, value)

