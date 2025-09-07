
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=512, num_heads=8)

    def forward(self, qk, value):
        v1, _ = self.attn(qk, value)
        return v1

# Initializing the model
m = Model()

# Inputs to the model
qk = torch.randn(512, 32, 64)
value = torch.randn(512, 32, 64)
