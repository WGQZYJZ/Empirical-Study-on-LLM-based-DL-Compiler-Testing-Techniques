
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 5)
        self.linear2 = torch.nn.Linear(5, 7)
 
    def forward(self, x1):
        v1 = self.linear1(x1) + 3
        v2 = torch.clamp_min(v1, 0)
        v3 = torch.clamp_max(v2, 6)
        v4 = v4 / 6
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 5)
