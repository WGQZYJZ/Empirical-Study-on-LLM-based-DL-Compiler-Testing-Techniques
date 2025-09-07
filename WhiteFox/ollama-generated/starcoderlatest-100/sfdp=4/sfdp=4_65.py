
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 32)
        self.key = torch.nn.Linear(768, 32)
 
    def forward(self, query, key, value, attn_mask):
        v1 = torch.einsum('b c n d, b c n e -> b c n d e', query, self.query) / math.sqrt(self.query.size(-1))
        v2 = torch.einsum('b c n d, b c n e -> b c n d e', key, self.key) / math.sqrt(self.key.size(-1))
        v3 = torch.einsum('b c n d, b c n e -> b c n d e', query, self.query).transpose(-2, -1) # Shape is (B, C, T, H)
        attn_weight = v1 * v2 / math.sqrt(v1.size(-1)) + 1e-9
        attn_weight = torch.softmax(attn_weight, dim=-1)
        output = attn_weight @ value
        return output


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(1, 768, 30, 56)
k1 = torch.randn(1, 768, 20, 49)
v1 = torch.randn(1, 768, 50, 63)
attn_mask1 = torch.softmax(q1, dim=-1) # Shape is (B, C, T, H)
