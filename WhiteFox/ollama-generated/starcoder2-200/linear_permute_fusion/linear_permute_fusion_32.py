
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.linear(x1, torch.randn((32, 48)))
        v = v.permute(0, 2, 1)
        return v


# Initializing the model