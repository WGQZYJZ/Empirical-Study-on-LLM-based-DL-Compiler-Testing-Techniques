
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output

# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(8, 56, 128, 64)
key   = torch.randn(8, 56, 128, 64)
value = torch.randn(8, 56, 128, 64)
attn_mask = torch.randint(2, (8, 56, 128, 64), dtype=torch.bool).to(dtype=query.dtype)
