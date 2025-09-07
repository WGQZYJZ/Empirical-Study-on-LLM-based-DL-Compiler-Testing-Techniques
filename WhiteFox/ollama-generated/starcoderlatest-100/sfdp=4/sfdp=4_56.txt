
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 4)
        self.key = torch.nn.Linear(3, 8)
        self.value = torch.nn.Linear(6, 12)
 
    def forward(self, query, key, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 3, 64, 64) # (batch, heads, seq, head_dim)
key = torch.randn(2, 3, 64, 64) # (num_heads, num_heads, seq, dim_per_head)
value = torch.randn(2, 8, 64, 64) # (num_heads, num_heads, seq, dim_per_head)
