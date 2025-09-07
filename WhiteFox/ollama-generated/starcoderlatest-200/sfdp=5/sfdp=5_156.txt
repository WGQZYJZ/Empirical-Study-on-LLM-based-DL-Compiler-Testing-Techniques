
class MultiheadAttention(torch.nn.Module):
    def __init__(self, num_heads=8, dim_kv=64):
        super().__init__()
 
        self.num_heads = num_heads
        self.dim_kv = dim_kv
 
    def forward(self, query, key, value):
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
 
        if "attn_mask" in kwargs:
            attn_weight = torch.softmax(qk + **kwargs["attn_mask"], dim=-1)
        else:
            attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
 
        output = attn_weight @ value # Compute the dot product of the dropout output and the value
 
        return output


# Model initialization (please change `num_heads` to match the number of heads you specified)
m = MultiheadAttention(num_heads=8)
 
# Inputs to the model
query  = torch.randn(batch_size, num_heads, seq_len, dim_kv)
key    = torch.randn(batch_size, num_heads, key_len,   dim_kv)
value  = torch.randn(batch_size, num_heads, value_len, dim_kv)
 
# Outputs from the model
output = m(query, key, value)

