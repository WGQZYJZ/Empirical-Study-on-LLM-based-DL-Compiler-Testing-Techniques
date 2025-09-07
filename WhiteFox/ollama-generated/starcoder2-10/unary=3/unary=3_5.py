
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1   = self.conv(x1)
        v2_1 = v1 * 0.5
        v4_2 = torch.erf(v2_1) + 1
        v3_3 = v4_2 + 0.7071067811865476 
        return v1, x1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) # Input tensor

# Obtaining the outputs of the model
v1, v2   = m(x1)