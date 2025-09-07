
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x):
        v1 = self.linear(x)
        return torch.sigmoid(v1)


# Initializing the model
m = Model()
x1 = torch.randn(1, 32)
