
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(6, 32)
        self.linear2 = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = torch.cat([v1], dim=0)
        return self.linear2(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 6, 64)
