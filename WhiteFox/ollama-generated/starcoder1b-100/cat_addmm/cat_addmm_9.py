
class Model(torch.nn.Module):
    def __init__(self, n_features):
        super().__init__()
        self.fc = torch.nn.Linear(n_features, 2)
 
    def forward(self, x1):
        v1  = self.fc(x1)
        v2  = torch.cat([v1], dim=0)
        return v2


# Inputs to the model
__input__ = torch.randn(3, 4)
