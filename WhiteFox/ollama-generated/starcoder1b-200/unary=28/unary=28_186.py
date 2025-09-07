
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 8)

    def forward(self, x1, min_value=0, max_value=255):
        v1 = self.linear(x1)
        v2 = v1 * (max_value - min_value + 1e-4) + min_value
        return v2


# Initializing the model
m = Model()
__input__ = torch.randn(1, 3)
