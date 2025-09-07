
class AttentionModel(torch.nn.Module):
    def __init__(self, qk_channels: int):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=qk_channels)
 
    def forward(self, query, key, value, attn_mask, dropout_p):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        output = attn_weight @ value # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = AttentionModel(qk_channels=32)

# Inputs to the model
query  = torch.randn(1, 3, 64, 64)
key    = torch.randn(8, 3, 64, 64)
value  = torch.randn(8, 3, 64, 64)
attn_mask = torch.ones([1, 8])
dropout_p = 0.25
