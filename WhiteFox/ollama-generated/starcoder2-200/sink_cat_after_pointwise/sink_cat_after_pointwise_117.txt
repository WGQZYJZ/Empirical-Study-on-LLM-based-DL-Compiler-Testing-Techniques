
class Model(torch.nn.Module):
    def __init__(self, k=3):
        super().__init__()

        self.k = k

    def forward(self, x1, x2):
        v0  = torch.tensor([4] * (x1.size(-1) // self.k), device="cuda")
        v1  = torch.cat([v0 for _ in range(5)], dim=-3).view(1, -1, 6)

        v2  = x1 + x2
        v3  = v1[v2]
        return v3


# Initializing the model
m  = Model()

# Inputs to the model