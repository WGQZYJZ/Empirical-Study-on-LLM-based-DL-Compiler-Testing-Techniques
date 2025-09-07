
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.addmm(x1, torch.randn(50, 3), torch.randn(3, 784))
        return torch.cat([v1], 2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 50, 784)
