
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.dropout(v1, 0.3)
        return v2


# Inputs to the model
x1 = torch.randn(1, 2, 2)
