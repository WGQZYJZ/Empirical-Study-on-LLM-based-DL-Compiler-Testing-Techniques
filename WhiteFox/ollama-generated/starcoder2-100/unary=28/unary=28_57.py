
class Model(torch.nn.Module):
    def __init__(self, max_, min_):
        super().__init__()
        self.linear = torch.nn.Linear()
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return 0.7 * v2

# Initializing the model
m = Model(max_=10.0, min_=-5.0)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

