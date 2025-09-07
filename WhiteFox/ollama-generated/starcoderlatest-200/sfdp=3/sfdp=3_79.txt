
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=64, num_heads=2)

    def forward(self, query, key, value):
        v1, _  = self.attn(query, key, value)
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 8, 64, 64)
key = torch.randn(20, 3, 64, 64)
value = torch.randn(20, 3, 64, 64)
