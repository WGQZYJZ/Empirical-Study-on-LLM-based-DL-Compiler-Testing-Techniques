
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1) * 0.2
        return torch.where(v1 > 0, v1, -v1)


# Initializing the model
m = Model()
x1 = torch.randn(3, 4)
