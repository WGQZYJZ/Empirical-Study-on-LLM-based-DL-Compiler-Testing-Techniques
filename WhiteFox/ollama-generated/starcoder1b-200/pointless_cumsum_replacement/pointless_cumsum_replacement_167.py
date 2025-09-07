
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.full = torch.full((3,), 0, dtype=dtype, device=device)
        self.cumsum = torch.cumsum(0, dim=0)

    def forward(self, x1):
        return self.cumsum(self.full)


# Initializing the model
m = Model()


