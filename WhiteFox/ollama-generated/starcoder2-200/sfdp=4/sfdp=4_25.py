
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask    # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)   # Apply softmax to the result
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value tensor
        return output


m  = ScaledDotProductAttention()
qk  = torch.randn(8, 64, 512)
key  = torch.randn(8, 3072, 512) # In our case, we need a higher number of keys (for 8 parallel attention heads). We use 3072 here because it is the total number of input positions * sequence length / number of heads
value  = torch.randn(8, 64, 512)
attn_mask  = torch.randn(3072, 3072) # In our case, we need a higher number of keys (for 8 parallel attention heads). We use 3072 here because it is the total number of input positions * sequence length / number of heads
__output__  = m(qk, key, value, attn_mask)


# Initializing the model