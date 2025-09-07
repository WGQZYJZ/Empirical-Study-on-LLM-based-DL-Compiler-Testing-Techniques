
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        # Perform random operation
        return torch.randn_like(x1)


