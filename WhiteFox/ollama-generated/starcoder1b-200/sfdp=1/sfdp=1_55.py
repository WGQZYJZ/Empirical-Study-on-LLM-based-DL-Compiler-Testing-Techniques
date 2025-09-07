
class Model(torch.nn.Module):
    def __init__(self, dim=128):
        super().__init__()
        self.fc = torch.nn.Linear(dim, dim)
 
    def forward(self, x):
        x = self.fc(x)
        return x


# Initializing the model
m = Model()


# Inputs to the model
q  = torch.randn(16, 8, 4, 4)
k = torch.randn(16, 8, 2, 3)
