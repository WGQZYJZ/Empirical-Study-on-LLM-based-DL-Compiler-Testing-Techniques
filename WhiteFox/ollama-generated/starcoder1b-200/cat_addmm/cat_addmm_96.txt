
class Model(torch.nn.Module):
    def __init__(self, n_feature1, n_feature2):
        super().__init__()
        self.fc = torch.nn.Linear(n_feature1 * 3, n_feature2)

    def forward(self, x1, x2):
        v1 = self.fc(torch.cat([x1, x2], dim=1))
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 8, 8)
x2 = torch.randn(1, 2, 4, 4)
