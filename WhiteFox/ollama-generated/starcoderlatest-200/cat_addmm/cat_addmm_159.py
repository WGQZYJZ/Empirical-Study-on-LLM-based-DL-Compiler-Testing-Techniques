
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(8, 16)
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = torch.addmm(v1, a_1, b_1)
        v3 = torch.cat([v2], dim=0)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8)
