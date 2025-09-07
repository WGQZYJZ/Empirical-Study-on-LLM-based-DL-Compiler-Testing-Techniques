
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_proj = torch.nn.Linear(768, 3052)
 
    def forward(self, qk, attn_mask, value):
        v1 = torch.matmul(qk, key.transpose(-2, -1)) / math.sqrt(qk.size(-1))
        v2 = v1 + attn_mask
        v3 = torch.softmax(v2, dim=-1)
        v4 = torch.dropout(v3, dropout_p, True)
        v5 = torch.matmul(v4, value)
        return v5


# Initializing the model
m = Model()

# Inputs to the model
qk  = torch.randn(128, 768, 9, 304)
attn_mask  = torch.arange(128 * 9 * 304).reshape(-1, 1, 9, 304).repeat(1, 768, 1, 1) >= 0
value = torch.randn(128, 768, 9, 304)
