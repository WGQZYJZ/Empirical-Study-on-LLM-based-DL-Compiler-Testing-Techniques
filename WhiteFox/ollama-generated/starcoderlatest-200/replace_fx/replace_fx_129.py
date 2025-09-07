
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout2d()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, 0.5)
        t2 = self.dropout(x1)
        return (t1 + t2).sum()


# Inputs to the model
x1 = torch.randn(4, 3, 3, 3)
