
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
        qk = torch.einsum('nd...dkm,dym->nd...km', query, key) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + (attn_mask if attn_mask is not None else torch.zeros_like(qk)) # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(3, 64, 128)
key   = torch.randn(6, 64, 512)
value = torch.randn(8, 64, 512)
attn_mask = None
