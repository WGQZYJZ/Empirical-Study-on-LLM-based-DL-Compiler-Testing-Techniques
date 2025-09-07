
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.full = torch.nn.functional.fill_with_(dtype=torch.float32, value=0.5)

    def forward(self, x1):
        v1 = self.full[None] * 0.5
        v2 = v1 * 0.7071067811865476
        v3 = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m = Model()

