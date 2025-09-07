
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, attn_mask):
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk  = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output


# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(20, 36, 192)
key    = torch.randn(10,  36, 192)
attn_mask = torch.eye(attn_mask).to(query.device).expand(-1, -1, key.size(-2), key.size(-1))
