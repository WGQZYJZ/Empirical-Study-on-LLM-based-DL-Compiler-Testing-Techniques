
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = self.linear(torch.cat([v1, v1], dim=-1))  # Sink the cat operation after pointwise linear
        return v2


# Initializing the model
m = Model()


