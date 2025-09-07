
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(
            embed_dim=8, num_heads=4, dropout=0.2)
 
    def forward(self, query, key, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = attn_weight @ value
        return output


# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(20, 8, 64, 64) # Shape: [batch size, num heads, query length, key length]
key    = torch.randn(20, 8, 196, 64) # Shape: [batch size, num heads, query length, key length]
value  = torch.randn(20, 8, 128, 32) # Shape: [batch size, num heads, value length, key length]
