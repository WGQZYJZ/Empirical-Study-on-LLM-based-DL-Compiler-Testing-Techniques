
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask):
        v1  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key tensors
        v2  = v1 + attn_mask  # Add the attention mask to the scaled dot-product
        v3  = torch.softmax(v2, dim=-1)  # Apply softmax to the result
        v4  = v3 @ value  # Compute the dot product of the attention weights and the value tensor
        return v4


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(5, 6)
key = torch.randn(10, 8)
value = torch.randn(32, 9)
attn_mask = torch.randint(low=0, high=2, size=(4, 7))
__output__  = m(query, key, value, attn_mask)

