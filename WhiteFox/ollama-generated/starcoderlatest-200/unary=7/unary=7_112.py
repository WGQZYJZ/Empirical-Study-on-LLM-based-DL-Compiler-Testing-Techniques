
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 16)
 
    def forward(self, x2):
        v3 = self.linear(x2)
        l4 = clamp(min=0, max=6, v3 + 3)
        v5 = v3 * l4 / 6
        return v5


# Initializing the model
m = Model()
 
# Inputs to the model
x2 = torch.randn(1, 8)
