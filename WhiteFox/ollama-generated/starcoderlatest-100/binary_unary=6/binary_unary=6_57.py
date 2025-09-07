
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(32000, 64)

    def forward(self, x1):
        v1 = torch.relu(torch.sum(self.conv(x1), dim=1)) 
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 32000)
