
import torch
 
query  = torch.randn(2048) # Initialize the query vector
key = <KEY> 16, 512) # Initialize the key matrix
 
 attn_mask  = ~torch.eye(attn_length).byte() # Create a boolean mask for attentions

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query_, key_, value_):
        qk  = torch.einsum("...x, ...y->...xy", query_, key_) / math.sqrt(query_.size(-1)) # Compute the dot product of the query and key
        qk += attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output  = attn_weight @ value_ # Compute the dot product of the attention weights and the value tensor
        return output
 
# Initializing the model
m = Model()

