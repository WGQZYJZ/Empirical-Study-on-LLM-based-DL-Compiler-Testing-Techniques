
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        return self.mm(torch.cat([x1, x2], dim=1))


# Inputs to the model
x1 = torch.randn(2, 5)
x2 = torch.randn(2, 5)
