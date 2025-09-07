
class Model(torch.nn.Module):
    def __init__(self, attn_dropout=0.1, residual_dropout=None):
        super().__init__()
 
        self.norm = torch.nn.LayerNorm(256)
 
    def forward(self, query, key, value):
        v  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        v  = v + attn_mask
        attn_weight = torch.softmax(v, dim=-1)
 
        attn_weight  = torch.dropout(attn_weight, attn_dropout, True)
        output  = attn_weight @ value
 
        v2  = self.norm(output)
 
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
query  = torch.randn(100, 384, 64)
key   = torch.randn(100, 384, 64)
value = torch.randn(100, 384, 64)
 
attn_mask  = torch.randint(-5000, -27, (query.size(0), query.size(-2)))

# Initializing the model
m = Model()

