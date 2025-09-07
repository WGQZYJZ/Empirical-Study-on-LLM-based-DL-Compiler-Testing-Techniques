
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(0.3)

    def forward(self, x1):
        x2 = self.dropout(x1)  # Dropout should be invoked as well!
        return x2


# Inputs to the model
x1 = torch.randn(1, 2, 2)
