
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(in_features=6, out_features=3)
 
    def forward(self, x1):
        return torch.cat([self.fc(x1)], dim=0)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 8, 64, 64)
