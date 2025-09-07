
class Model(torch.nn.Module):
    def __init__(self, n_features):
        super().__init__()
        self.linear = torch.nn.Linear(n_features, 32)

    def forward(self, x1):
        v1 = self.linear(x1)
        return v1 + torch.randn_like(v1)


# Initializing the model
m = Model(n_features=40)
x1 = torch.randn(1, 3, 28, 28)
