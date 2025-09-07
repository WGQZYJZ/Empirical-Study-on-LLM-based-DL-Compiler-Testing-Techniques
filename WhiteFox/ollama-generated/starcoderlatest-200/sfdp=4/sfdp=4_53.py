
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_1 = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, query, key, value, attn_mask):
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk  = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight  = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ value # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(4, 3, 64, 64) # (batch_size=4, query_len=3, seq_len=64, emb_dim=64)
key = torch.randn(5, 3, 64, 64)    # (batch_size=5, query_len=3, seq_len=64, emb_dim=64)
value = torch.randn(6, 8, 64, 64) # (batch_size=6, query_len=3, seq_len=64, emb_dim=64)
attn_mask = torch.rand(6, 64, 64) # (batch_size=6, seq_len=64, seq_len=64)
