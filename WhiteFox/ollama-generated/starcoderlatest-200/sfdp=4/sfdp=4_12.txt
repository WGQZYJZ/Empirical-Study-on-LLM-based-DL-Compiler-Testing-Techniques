
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, query, key, value, attn_mask=None):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) + (attn_mask if attn_mask is not None else None)
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output

# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(4, 3, 64, 64)
key    = torch.randn(2, 3, 64, 64)
value  = torch.randn(1, 3, 64, 64)
attn_mask  = torch.ones((4, 2), dtype=torch.float, device='cuda')
