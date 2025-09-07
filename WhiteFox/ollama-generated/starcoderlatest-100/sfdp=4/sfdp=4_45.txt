
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(16, 16)
        self.key   = torch.nn.Linear(32, 16)

    def forward(self, q, k):
        qk = (q @ k.transpose(-2, -1)) / math.sqrt(q.size(-1)) + 0.5
        attn_weights = torch.softmax(qk, dim=-1)

        # Apply multi-head attention to the output
        attn_output = (attn_weights @ v) * k.size(-1)
        return attn_output

# Initializing the model
m = Model()

# Inputs to the model
q  = torch.randn(2, 16, 1024)
k  = torch.randn(2, 16, 768)
v  = torch.randn(2, 32, 768)
