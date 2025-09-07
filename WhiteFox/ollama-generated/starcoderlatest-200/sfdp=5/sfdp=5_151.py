
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(50, 8)
 
    def forward(self, x1, x2):
        v1 = x1 @ key.transpose(-2, -1) / math.sqrt(x1.size(-1)) + attn_mask
        v2 = torch.softmax(v1, dim=-1)
        v3 = torch.dropout(v2, dropout_p, True)
        return torch.matmul(v3, value)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(batch, nhead, 64, d_k)  # (batch, head num, sequence length, key dim)
key = torch.randn(nhead, 50, 8).transpose(-2, -1)
value = torch.randn(nhead, 50, 64)


