
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_projection = torch.nn.Linear(512, 32)
        self.v = torch.nn.Linear(32, 768)
 
    def forward(self, query, key, value, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        output = attn_weight @ value  # Compute the dot product of the dropout output and the value
        return self.attn_projection(output), self.v(output)


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 512, 64, 64) # query shape [batch_size, num_heads, seq_len, embedding_dim]
key = torch.randn(1, 32, 8, 8) # key shape [batch_size, num_heads, embed_dim, embed_dim]
value = torch.randn(1, 32, 40, 40) # value shape [batch_size, num_heads, seq_len, embedding_dim]
attn_mask = (attn_mask != 0).unsqueeze(-2).float() # attn_mask shape [batch_size, 1, 1, embed_dim]
__output__, 