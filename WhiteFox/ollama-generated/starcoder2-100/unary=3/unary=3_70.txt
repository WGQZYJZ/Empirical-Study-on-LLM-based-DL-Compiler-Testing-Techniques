
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.randn(3, 256)  # Initializing tensor
        v1  = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 + 0.7854  # Reassigning the value to a variable
        v4  = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
