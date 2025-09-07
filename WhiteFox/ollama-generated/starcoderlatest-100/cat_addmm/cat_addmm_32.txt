
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.fc = torch.nn.Linear(784, 64)
 
    def forward(self, x1):
        v1 = x1 @ mat1.t() + bias1
        v2 = torch.cat([v1], dim=dim)
        return self.fc(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64).view(-1, 784)
