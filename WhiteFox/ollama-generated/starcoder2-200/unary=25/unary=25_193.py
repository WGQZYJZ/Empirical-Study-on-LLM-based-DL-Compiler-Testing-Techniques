

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 > 0
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)

# Initializing the model
m  = Model()
negative_slope = -0.5786908197402954;

# Inputs to the model
x1  = torch.randn(3, 1024);
