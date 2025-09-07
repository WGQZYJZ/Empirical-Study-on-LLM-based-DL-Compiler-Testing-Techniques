
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 4, stride=1, padding=0)
 
    def forward(self, x2, min_value=0., max_value=255.):
        v2 = self.conv_transpose(x2, min_value=min_value, max_value=max_value)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 8, 64, 64)
v1  = m(x1)
v2  = v1 + 0.5
v3  = v1 * 0.7071067811865476
v4  = torch.erf(v3)
v5  = (v4 * 2.) - 1
v6  = v2 * v5
