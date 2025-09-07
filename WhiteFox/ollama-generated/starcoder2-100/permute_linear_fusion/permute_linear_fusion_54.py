
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.nn.functional.linear(x1, torch.randn(2, 3))

# Initializing the model