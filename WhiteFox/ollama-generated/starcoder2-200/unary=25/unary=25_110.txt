
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 32 * 8, 4)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 > 0
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4

# Initializing the model with a negative slope of `0.5`
m  = Model(negative_slope=0.5)

# Input to the model
x = torch.randn(16, 32 * 32 * 8)
 
