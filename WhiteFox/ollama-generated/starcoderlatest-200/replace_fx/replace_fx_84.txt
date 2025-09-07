
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout2d(0.25)
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = self.dropout(x1)
        v2 = self.linear(v1)
        return v2

# Initializing the model
m = Model()


# Inputs to the model
__input__ = torch.randn(100, 3, 64, 64)
