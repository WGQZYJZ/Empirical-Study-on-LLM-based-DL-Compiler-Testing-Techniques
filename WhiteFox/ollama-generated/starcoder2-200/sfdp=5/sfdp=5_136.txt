
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None, dropout_p=0.5):
        v1  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        v2  = v1 + attn_mask  # Add the attention mask to the scaled dot product
        v3  = torch.softmax(v2, dim=-1) # Apply softmax to the result
        v4  = torch.dropout(v3, dropout_p, True) # Apply dropout to the softmax output
        v5  = v4 @ value  # Compute the dot product of the dropout output and the value
        return v5


# Initializing the model
m  = Model()
 

# Inputs to the model
query  = torch.randn(1, 64, 64)
key    = torch.randn(1, 64, 64)
value  = torch.randn(1, 32, 64, 64)
__output__  = m(query, key, value, attn_mask=None, dropout_p=0.5)

