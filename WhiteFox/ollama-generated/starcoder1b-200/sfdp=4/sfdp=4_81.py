
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(20, 1)

    def forward(self, x1, x2):
        w1 = self.attn(x1) * math.sqrt(x1.size(-1))
        w2 = self.attn(x2) * math.sqrt(x2.size(-1))
        return (w1 + w2) / 2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
x2 = torch.randn(2, 3, 64, 64)
