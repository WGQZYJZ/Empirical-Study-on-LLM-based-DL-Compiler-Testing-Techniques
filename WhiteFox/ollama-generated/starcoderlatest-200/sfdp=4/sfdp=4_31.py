
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(16, 32)
        self.value = torch.nn.Linear(16, 32)
        self.key = torch.nn.Linear(32, 16)
 
    def forward(self, query, key):
        v1 = torch.matmul(query, self.attn(self.key(query))).transpose(-2, -1) / math.sqrt(query.size(-1)) + attn_mask  # Apply the scaled dot product to compute attention weights
        v2 = torch.matmul(v1, self.value(self.key(v1)))
        return v2


# Inputs to the model
x1 = torch.randn(16, 32)
x2 = torch.randn(16, 32)
