
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 > 0
        v3 = negative_slope = 0.2
        v4 = -v3 if v2 else v1
        return v4

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 8)
