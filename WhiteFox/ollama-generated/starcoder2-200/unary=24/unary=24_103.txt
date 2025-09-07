
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v0 = self.conv(x)
        v1  = v0 > 0 
        v2 = v0 * -0.5
        v3  = torch.where(v1, v0, v2)
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model
x = torch.randn(4, 3, 64, 64)
 
# Initializing a negative slope for testing
negative_slope  = -0.5
 
