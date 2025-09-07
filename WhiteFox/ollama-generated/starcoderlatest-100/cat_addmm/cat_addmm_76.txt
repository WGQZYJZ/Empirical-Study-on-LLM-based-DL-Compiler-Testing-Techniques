
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(256, 32)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, torch.eye(256), torch.eye(256))
        v2 = torch.cat([v1], dim=1)
        return self.linear1(v2)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 3200)
