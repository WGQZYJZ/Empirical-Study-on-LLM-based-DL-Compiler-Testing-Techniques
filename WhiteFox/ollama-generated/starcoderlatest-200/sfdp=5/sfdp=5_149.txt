
class Model(torch.nn.Module):
    def __init__(self, d_model: int, num_heads: int):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(d_model, num_heads)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attn_mask: torch.Tensor):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        output = attn_weight @ value # Compute the dot product of the dropout output and the value
        return output

# Initializing the model
m = Model(d_model=512, num_heads=8)

# Inputs to the model
query  = torch.randn(64, d_model, 7, 7)
key    = torch.randn(1024, d_model, 13, 13)
value  = torch.randn(1024, d_model, 13, 13)
attn_mask  = torch.ones_like(qk)
