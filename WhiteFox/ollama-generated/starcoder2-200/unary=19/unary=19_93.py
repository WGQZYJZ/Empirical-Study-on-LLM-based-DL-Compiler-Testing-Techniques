class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(5, 3)

    def forward(self, x1):
        v2 = torch.sigmoid(self.lin(x1))
        return v2
