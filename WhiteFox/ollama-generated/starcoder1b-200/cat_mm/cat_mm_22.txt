
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(3, 2)
 
    def forward(self, x1):
        v1 = torch.mm(x1, x1)
        v2 = torch.cat([v1, v1, ..., v1])
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
