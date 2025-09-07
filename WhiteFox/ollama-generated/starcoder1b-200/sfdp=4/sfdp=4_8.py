
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer  = torch.nn.Linear(32, 64)
        self.key    = torch.nn.Parameter(torch.zeros((8, 1024)))
        self.value   = torch.nn.Parameter(torch.zeros((8, 1024)))
        self.attn   = torch.nn.MultiheadAttention(1024, 16)
 
    def forward(self, x1):
        v1 = self.layer(x1)
        query = self.attn(v1, v1, v1, mask=torch.ones((8, 1, 1), device="cpu"))
        key   = self.key * math.sqrt(x1.size(-1))
        value = self.value * math.sqrt(x1.size(-1))
        return query @ key / math.sqrt(x1.size(-1))  # Compute the dot product of the attention weights and the value


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(8, 32, device="cpu")
