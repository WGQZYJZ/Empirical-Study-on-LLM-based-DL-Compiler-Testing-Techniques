
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=512, num_heads=8)
 
    def forward(self, query, key, attn_mask=None):
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk += attn_mask # Add the attention mask to the scaled dot product
        attn_weight  = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = torch.dropout(attn_weight @ value, dropout_p, True) # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(256, 32, 8, 64, 64).permute(0, 4, 1, 2, 3) # Shape: (batch_size, num_heads, query_len, key_len, embedding_dim)
x2 = torch.randn(128, 32, 8, 64, 64).permute(0, 4, 1, 2, 3) # Shape: (batch_size, num_heads, query_len, key_len, embedding_dim)
