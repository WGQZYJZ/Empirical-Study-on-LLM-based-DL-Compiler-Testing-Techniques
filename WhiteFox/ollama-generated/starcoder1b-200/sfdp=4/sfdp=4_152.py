
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(4096, 1)

    def forward(self, x1):
        x2 = x1 @ torch.randn_like(x1)
        return self.fc(torch.sigmoid(x2))


# Inputs to the model
x1 = torch.randn(2, 3, 100, 100)
