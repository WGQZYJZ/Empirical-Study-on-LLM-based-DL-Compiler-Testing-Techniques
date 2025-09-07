
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(3, 4)
 
    def forward(self, x1):
        v1 = self.lin(x1) + 50
        v2 = torch.clamp_min(v1, 0)
        v3 = torch.clamp_max(v2, 6)
        return v3 / 6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 5, 3).float().to("cuda")

