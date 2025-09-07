
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(x1.shape[0], -1)) + 3
        v2 = torch.clamp_min(v1, 0)
        v3 = torch.clamp_max(v2, 6)
        v4 = v3 / 6
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 28, 28)
