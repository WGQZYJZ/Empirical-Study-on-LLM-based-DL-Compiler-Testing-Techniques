
class Model(torch.nn.Module):
    def __init__(self, n_features):
        super().__init__()
        self.n_features = n_features

    def forward(self, x1, x2):
        v1 = torch.addmm(x1, x2, x3)
        return v4


# Initializing the model
m = Model(5)


# Inputs to the model
x1  = torch.randn(1, 3, self.n_features, 64, 64)
x2  = torch.randn(1, 4, 8, 64, 64)
