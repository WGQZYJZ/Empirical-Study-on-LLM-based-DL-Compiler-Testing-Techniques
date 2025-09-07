
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, attn_mask=None):
        attn  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key tensor
        if not attn_mask:
            attn  = torch.softmax(attn, dim=-1) # Apply softmax to the result
        else:
            attn  += attn_mask  # Add the attention mask to the scaled dot-product
        output  = attn @ value 
        return v6


# Initializing the model
m  = Model()


# Inputs to the model