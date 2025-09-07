
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, attn_mask=None, value=None):
        v1 = torch.einsum('...at,...td->...ad', [query, key])  # Compute the dot product of the query and key tensors.
        v2 = v1 / math.sqrt(query.size(-1))  # Scale the result by dividing it by the square root of the size of the last dimension in the query tensor.
 
        if attn_mask is not None:
            v3 = v2 + attn_mask   # Add the attention mask to the scaled dot product
        
        else:
            v3 = v2

        v4 = torch.softmax(v3, dim=-1)  # Apply softmax to the result
        v5 = torch.einsum('...ad,...vd->...vd', [v4, value])   # Compute the dot product of the attention weights and the value tensor.
        return v5

# Initializing the model
m  = Model()

