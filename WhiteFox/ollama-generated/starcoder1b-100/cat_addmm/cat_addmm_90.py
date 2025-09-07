
class Model(torch.nn.Module):
    def __init__(self, x_dim=16):
        super().__init__()
        self.fc1 = torch.nn.Linear(x_dim, 32)
        self.fc2 = torch.nn.Linear(32, 8)
 
    def forward(self, x):
        v1 = torch.addmm(x, x, x)
        v2 = self.fc1(v1)
        v3 = torch.cat([v2], dim=0)
        return self.fc2(v3)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 16, requires_grad=True)
